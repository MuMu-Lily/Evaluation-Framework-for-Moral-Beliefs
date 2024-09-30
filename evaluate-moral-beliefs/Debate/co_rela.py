
import numpy as np


#一个函数，计算两个列表数据之间的相关性
def co_re1(x,y):
    
    #计算x的均值
    x_mean = sum(x)/len(x)
    #计算y的均值
    y_mean = sum(y)/len(y)
    
    #计算x和y的协方差
    cov = sum([(x[i]-x_mean)*(y[i]-y_mean) for i in range(len(x))])
    
    #计算x和y的标准差
    x_var = sum([(x[i]-x_mean)**2 for i in range(len(x))])
    y_var = sum([(y[i]-y_mean)**2 for i in range(len(y))])
    
    #计算相关系数
    r = cov/(x_var*y_var)**0.5
    
    return r

def co_re2(x,y):
    #计算x和y的相关性
    r = np.corrcoef(x,y)
    
    return r 


#同时列表X的数据分布，包含平均值、方差、标准差、中位数、众数、四分位数、极差、变异系数等
def analysis(x):
    #计算x的均值
    x_mean = sum(x)/len(x)
    #计算x的方差
    x_var = sum([(x[i]-x_mean)**2 for i in range(len(x))])/len(x)
    #计算x的标准差
    x_std = x_var**0.5
    #计算x的中位数
    x_median = np.median(x)
    #计算x的众数
    x_mode = np.argmax(np.bincount(x))
    #计算x的四分位数
    x_quarter = np.percentile(x,(25,50,75),interpolation='midpoint')
    #计算x的极差
    x_range = max(x)-min(x)
    #计算x的变异系数
    x_cv = x_std/x_mean
    
    return x_mean,x_var,x_std,x_median,x_mode,x_quarter,x_range,x_cv


if __name__ == '__main__':
    x = [4,5,5,5,5]
    y = [1,0,1,1,1]
    
    print(co_re1(x,y))
    print(co_re2(x,y))