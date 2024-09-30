import functools
import numpy as np
import pdb
from tqdm import tqdm
from convergence import NormOfDifferenceTest # 用于执行两个向量或数据集之间差异的范数测试
from utils import exp_transform, log_transform, statdist # 指数变换、对数变换、计算状态分布

def _init_lsr(n_items, alpha, initial_params):
    '''
    :param n_items: 表示比较的项目数量
    :param alpha: 表示初始化马尔可夫链的权重
    :param initial_params: 表示回归模型的初始参数
    '''
    if initial_params is None:
        # ones函数：创建一个指定形状的数组，并将其中的元素都初始化为 1
        # 创建了一个长度为 n_items 的数组，并将所有元素设置为 1
        weights = np.ones(n_items)
    else:
        weights = exp_transform(initial_params) # 进行指数变换
    # 创建一个形状为 (n_items, n_items) 的二维数组 chain， 其中每个元素的值均为 alpha
    # chain是马尔可夫链的转移矩阵
    chain = alpha * np.ones((n_items, n_items), dtype=float)
    return weights, chain

def _ilsr(fun, params, max_iter, tol): 
    #pdb.set_trace()
    '''
    :param fun:表示用于迭代估计的函数或方法
    :param params:表示回归模型的参数，是一个可迭代对象
    :param max_iter:表示最大迭代次数
    :param tol:表示收敛的容差阈值-用于判断算法是否达到收敛状态的标准，当迭代过程中的参数变化小于或等于容差阈值时，可以认为算法已经收敛。
    '''
    # 用于判断迭代过程是否已经收敛
    # order = 1 表示使用一阶范数进行差异比较。
    converged = NormOfDifferenceTest(tol, order=1)
    for _ in tqdm(range(max_iter)): # max_iter 最大迭代次数
        params = fun(initial_params=params)
        if converged(params):
            return params
    # 表示算法未能在指定次数内收敛
    raise RuntimeError("Did not converge after {} iterations".format(max_iter))

def lsr_pairwise(n_items, data, alpha=0.00001, initial_params=None):
    # 调用_init_lsr进行初始化，获取初始权重和马尔可夫链
    weights, chain = _init_lsr(n_items, alpha, initial_params)
    # 通过遍历data中的每个比较对（winner, loser），根据比较结果更新马尔可夫链的转移率。通过增加对应链中的元素，以及使用权重进行归一化，来反映比较结果。
    for winner, loser in data:
        chain[loser, winner] += 1 / (weights[winner] + weights[loser])
    # 从转移率矩阵中减去对角线上的元素之和，用于使转移率矩阵满足概率分布的性质
    chain -= np.diag(chain.sum(axis=1))
    # 通过 statdist 函数计算马尔可夫链的稳态分布，并对其进行对数变换。返回对数变换后的稳态分布作为参数估计的结果。
    return log_transform(statdist(chain))

def ilsr_pairwise(n_items, data, alpha=0.0, initial_params=None, max_iter=180, tol=1e-8):
    fun = functools.partial(lsr_pairwise, n_items=n_items, data=data, alpha=alpha)
    return _ilsr(fun, initial_params, max_iter, tol)


def ranking_weights(weights):
    # 原始列表
    #original_list = [3, 1, 2, 5, 4]  # 2, 4, 3, 0, 1

    # 使用enumerate函数获取数字和其索引的元组列表
    indexed_list = list(enumerate(weights))
    print("indexed_list:", indexed_list)
    # 使用sorted函数按数字的值进行排序，reverse=True表示降序排序
    sorted_indexed_list = sorted(indexed_list, key=lambda x: x[1], reverse=True)

    # 输出排序后的索引列表
    sorted_indexes = [index for index, _ in sorted_indexed_list]
    print(sorted_indexes)

    idx_weights_dp = {idx:weights[idx] for idx in sorted_indexes}#将排序后的列表转换成字典，key是idx，value是排序后的值，也就是权重

    return idx_weights_dp

