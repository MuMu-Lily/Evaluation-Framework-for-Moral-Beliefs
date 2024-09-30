"""Inference algorithms for the Plackett--Luce model."""

from __future__ import division

import json
import os.path

import numpy as np
import re
from i_lsr_new import ilsr_pairwise, ranking_weights


def generation_tuples(path):
    nation_tempDict = {}
    with open(path, 'r', encoding='utf-8') as f:
        ALLList = []
        dictList = []
        for line in f: # 读取每一行, 一个四元组, 一个四元组是一个列表, 四个元素是字典, 
            ##四个字典是一个四元组, 四个字典的key是相同的, 分别是name, temperature, nation_temp, index, 四个字典的value是不同的, 分别是国家名, 温度, 国家名_温度, 国家名_温度对应的index
            if line.strip() != '': #如果不是空行, 说明一个四元组还没有结束, 继续读取, 读取的内容是一个字典
                dict_nation_temp = eval(line.strip()) #将字符串转换为字典
                if type(dict_nation_temp['name']) == str: #如果name是字符串，说明只有一个国家。写入国家和对应的temperature
                    nation_temp = '{}_{}'.format(dict_nation_temp['name'],dict_nation_temp['temperature'])
                    #将国家名和温度拼接成一个字符串, 用_连接, 作为新的key, 用于后面的排序, 以及后面的字典的索引, 也就是index
                    #print(nation_temp)
                    if nation_temp not in nation_tempDict: 
                        idx = len(nation_tempDict) + 1
                        nation_tempDict[nation_temp] = idx
                    else:
                        idx = nation_tempDict[nation_temp]

                else:
                    name_ls = dict_nation_temp['name'] #如果name是列表，说明有两个国家。写入两个国家中较长的那个国家和对应的temperature
                    #print(name_ls)
                    if len(name_ls[0]) >= len(name_ls[1]):
                        nation_temp = '{}_{}'.format(dict_nation_temp['name'][1], dict_nation_temp['temperature'])
                    else:
                        nation_temp = '{}_{}'.format(dict_nation_temp['name'][0], dict_nation_temp['temperature'])

                    if nation_temp not in nation_tempDict:
                        idx = len(nation_tempDict) + 1
                        nation_tempDict[nation_temp] = idx
                    else:
                        idx = nation_tempDict[nation_temp]

                dict_nation_temp['nation_temp'] = nation_temp  #将nation_temp写入dict_nation_temp, 作为新的key, 用于后面的排序, 以及后面的字典的索引
                dict_nation_temp['index'] = idx #将index写入dict_nation_temp

                #if dict_nation_temp
                dictList.append(dict_nation_temp) #将dict_nation_temp写入dictList, 作为一个四元组的一个元素, 也就是一个字典, 四个字典是一个四元组, 四个字典的key是相同的, 分别是name, temperature, nation_temp, index, 四个字典的value是不同的, 分别是国家名, 温度, 国家名_温度, 国家名_温度对应的index
            else: #如果是空行，说明一个四元组结束了
                ALLList.append(dictList)
                dictList = []

    return ALLList, nation_tempDict#返回一个加入了nation_temp和index的四元组列表。nation_tempDict是一个字典，key是nation_temp，value是index

def convert_line2dict(text):

    pattern1 = r"<([^<>]*)>$"  # 匹配最后一个角括号内的内容

    matches1 = re.findall(pattern1, text)
    if matches1:
        last_bracket_content = matches1[-1]
        #print(last_bracket_content)
    else:
        print("未找到匹配的角括号内容")

    pattern2 = r"<s snum=(\d+)>"

    matches2 = re.findall(pattern2, text)
    if matches2:
        snum_value = matches2[0]
        #print(snum_value)
    else:
        print("未找到匹配的snum值")

    if 'o' in last_bracket_content:
        return {snum_value:'o'}
    elif 'f' in last_bracket_content:
        return {snum_value:'f'}
    else:
        return {snum_value:'mid'}


def read_annotation(path): #读取人类标注的文件
    fr = open(path, 'r', encoding='utf-8')

    AnnTuple_List = []
    AnnAll_List = []
    for line in fr:
        if line.strip() != '':
            dic = convert_line2dict(line.strip())#
            print("dic_ann", dic)
            AnnTuple_List.append(dic)
        else:
            AnnAll_List.append(AnnTuple_List)
            AnnTuple_List = []
        
    return AnnAll_List #返回一个列表，列表中的元素是字典，字典的key是snum的值，value是f或者o



def combin_twoList(ALLList, AnnAllList):
    ALL_Tuples = ()
    for List_4 in zip(ALLList, AnnAllList):#四个标注对一组，现在取第一组
        print("List_4", List_4)
        TupList = []
        for Tuple_4 in zip(List_4[0], List_4[1]):#取一组当中的每一个
            print("Tuple_4", Tuple_4) 
            for key in Tuple_4[1]: #将人类标注的文件中的字典的key和value转换成元组的形式
                if Tuple_4[1][key]=='f':#如果value是f，value是1
                    value = 1
                elif Tuple_4[1][key]=='o':
                    value = -1
                else: #如果value是mid，value是0
                    value = 0
                tuple_one = (Tuple_4[0]['index']-1,value) #将四元组的index-1和value转换成元组的形式
                TupList.append(tuple_one)
        sorted_List = sorted(TupList, key=lambda x: x[1], reverse=True) #将元组按照value的值进行排序，value是1的在前面，value是-1的在后面

        print("sortedlist", sorted_List)
        
        Tuple_5pairs = ((sorted_List[0][0], sorted_List[1][0]), (sorted_List[0][0], sorted_List[2][0]), (sorted_List[0][0], sorted_List[3][0]), (sorted_List[1][0], sorted_List[3][0]), (sorted_List[2][0], sorted_List[3][0])) #做出来的排序对，索引代表的国家排序对，一共从n=4当中获取了五个排序对
        print("Tuple_5pairs", Tuple_5pairs)
        ALL_Tuples = ALL_Tuples + Tuple_5pairs #将五元组合并成一个元组

    return ALL_Tuples #返回一个元组，元组中代表的都是比较大小的对，例如（a,b）代表着a比b大(本文代表着偏见更大)



if __name__ == '__main__':
    input_path = './original_tuples_12/test_tuple.jsonl' #改这个
    output_folder = './human_ann_ranking/json'

    nb_items = 780 #数据的数量
    nb_rankings = 780 * 12 #12 #做成四元组后总数据的数量
    size_of_ranking = 2

    ALLList, nation_tempDict = generation_tuples(input_path)
    print("ALLList:", ALLList)
    print("nation_tempDict:", nation_tempDict)#以上所有的操作是加入了temperature，然后建立了index（我可以不需要temperature,或者全都设置成一样，然后直接建立目录，道德原则对应着国家？待确定）
    print('1' * 50)

    ann_path = './Ann_res/test_sort.txt' #改这个
    #4 o 4 f; 4 4 o f
    Ann_list = read_annotation(ann_path)#人类标注的label的读取，注意此时的label与原文件的数据是对应的
    print("Ann_list:", Ann_list)
    print('1' * 50)

    idxnation_Dict = {v: k for k, v in nation_tempDict.items()} #将nation_tempDict的key和value对调，作为新的字典，key是index，value是nation_temp
    combinTuples = combin_twoList(ALLList, Ann_list) #做出排序对
    print("idxnation_", idxnation_Dict)
    print("combinTuples:", combinTuples)
    print('1' * 50)
    #print(len(combinTuples))
    #print(len(set(combinTuples)))

    filter_combinTuple = set(combinTuples) #将排序对去重


    my_list_new = list(filter_combinTuple) #将新的元组转换成列表
    
    print("my_list_new:", my_list_new)
    print(len(my_list_new)) #多少个排序对
    print('1' * 50)
    result = []

    for i in range(len(my_list_new)): #找到出现矛盾的排序对
        for j in range(i + 1, len(my_list_new)):
            # print("my_list_new[i]", set(my_list_new[i]))
            # print("my_list_new[j]", set(my_list_new[j]))
            if set(my_list_new[i]) == set(my_list_new[j]):
                result.append(my_list_new[i])


    print(len(result))
    print("result",result)
    print('1' * 50)

    for tup_del in result: #将矛盾的排序对从列表中删除
        print("tup_del", tup_del)
        my_list_new.remove(tup_del)
    

    idx_pairs = [(2, 0), (3, 0), (4, 0), (4, 5), (7, 5), (8, 5)]

    list_arrange_105 = ilsr_pairwise(8, my_list_new, alpha=0.00001) #ilsr_pairwise函数的作用是对排序对进行处理，返回总体排序后的列表，8代表数据总条数，例如道德原则总数目
    #这个alpha可以改，但是建议不改
    #list_arrange_104 = ilsr_pairwise(780, my_list_new, alpha=0.0001) #780
    print("list_arrange_104", list_arrange_105)
    print("np_shape", np.shape(list_arrange_105)) #输出排序后的列表的形状
    DP = ranking_weights(list_arrange_105) #从0开始，需要+1,ranking weights函数作用是将排序后的列表转换成字典，key是idx，value是排序后的值，也就是权重
    print("DP:", DP) #最终排序的索引和对应的权重
    print('1' * 50)
    with open(os.path.join(output_folder,"ranking_test.jsonl"), 'w', encoding='utf-8') as f: #这个部分的作用是将排序后的列表写入json文件
        #改前面的文件名部分
        for k,v in DP.items(): #将排序后的列表写入json文件，写入的内容是一个字典，字典的key是idx，nation，temperature，weight，字典的value是对应的值，weight是排序后的值
            nation_temp = idxnation_Dict[k + 1]
            nation, temp = nation_temp.split('_')
            dp = {"idx":k+1, "nation":nation, 'temperature':temp, 'weight':v}


            f.write(json.dumps(dp, ensure_ascii=False) + '\n')


