#处理csv文件，先建立所有道德原则的索引，先把选项对应到的具体的道德原则，，再获得索引代表的道德原则的排序对
#然后再去直接拿排序对进行排序

from __future__ import division

import json
import os.path

import os
import re
import csv
import numpy as np
import re
from i_lsr_new import ilsr_pairwise, ranking_weights

#构建道德原则的索引。。读取csv文件，返回一个字典，key是index，value是道德原则
def indxmoralprinciple(file_name):
    moralbag = []
    with open(file_name, 'r', encoding='gbk') as f:
        reader = csv.reader(f)
        for row in reader:  #一行6列
            for i in range(4):
                if row[i] == '':
                    continue  #如果不是空行
                if row[i] not in set(moralbag):
                    moralbag.append(row[i])
                else:
                    # print('1' * 10)
                    we = 1
        # print("moralbag:", moralbag)
        print(len(moralbag))
    
    dic_moral = {i: moralbag[i] for i in range(len(moralbag))}
    moral_dic = {moralbag[i]: i for i in range(len(moralbag))}

    # print("idx_moral:", dic_moral)
    # print("moral_idx:", moral_dic)

    return dic_moral, moral_dic


#通过字符串匹配等方法，将类似于“选项：B；；；坚定分数：2；；；”或“选项：B坚定分数：2”字符串中的A和2提取出来。其中，A根据“选项：”后一个字符提取出来，2根据“坚定分数：”后的数字提取出来
def extract_option_score(text):
    pattern1 = re.compile(r'选项：([A-Z])')
    pattern2 = re.compile(r'坚定分数：(\d)')
    # pattern3 = re.compile(r'坚信心数：(\d)')
    pattern3 = re.compile(r'(\d)')
    pattern4 = re.compile(r'([A-Z])')
    
    matches1 = re.findall(pattern1, text)
    matches2 = re.findall(pattern2, text)
    matches3 = re.findall(pattern3, text)
    matches4 = re.findall(pattern4, text)
    # print("pattern3", matches3)
    if matches1 and matches2:
        option = matches1[0]
        score = matches2[0]
        return option, score
    elif matches1 and matches3:
        option = matches1[0]
        score = matches3[0]
        return option, score
    elif matches4 and matches2:
        option = matches4[0]
        score = matches2[0]
        return option, score
    elif matches4 and matches3:
        option = matches4[0]
        score = matches3[0]
        return option, score
    else:
        print("pattern1", matches1)
        print("pattern2", matches2)
        print("pattern3", matches3)
        
        print("字符串未找到匹配的选项和分数")
        print("text:", text)
        return None, None
    
    return 1


#给定选项和分数，和一个列表，选项对应着道德原则，返回一个选项对应的道德原则对
def rowsort_onechoice(option, score, row, flag):
    rowsortpairs = []
    #初始设置a_principle等全部为-1，表示没有对应的道德原则
    a_principle = []
    b_principle = []

    # 设置a_principle = row[12]如果row[12]不为空
    if row[8] != '':
        a_principle.append(row[8])  #A对应的支持的道德原则
    if row[9] != '':
        a_principle.append(row[9])
    if row[10] != '':
        b_principle.append(row[10])
    if row[11] != '':
        b_principle.append(row[11])

    
    if flag == 1: #正序
        if option == 'A':
            for i in range(len(a_principle)):
                for j in range(len(b_principle)):
                    rowsortpairs.append((a_principle[i], b_principle[j], score))
        elif option == 'B':
            for i in range(len(b_principle)):
                for j in range(len(a_principle)):
                    rowsortpairs.append((b_principle[i], a_principle[j], score))
        else:
            print("正序未找到匹配的选项")
    else:  #逆序
        if option == 'A':
            for i in range(len(b_principle)):
                for j in range(len(a_principle)):
                    rowsortpairs.append((b_principle[i], a_principle[j], score))
        elif option == 'B':
            for i in range(len(a_principle)):
                for j in range(len(b_principle)):
                    rowsortpairs.append((a_principle[i], b_principle[j], score))
        else:
            print("逆序未找到匹配的选项")
    
    # print("oringinal_rowsortpairs:", rowsortpairs)
    return rowsortpairs


#对全是相同或矛盾对进行加减,还会除以次数
def deal_weight(same_pairs):
    a = []
    # print("same_pairs:", same_pairs)
    a.append([same_pairs[0][0],int(same_pairs[0][1])])
    k = 1
    for i in range(1, len(same_pairs)):
        k = k + 1
        if a[0][0] == same_pairs[i][0]:
            # print("a[0]:", a[0], "加上same_pairs[i]:", same_pairs[i])
            a[0][1] = a[0][1] + int(same_pairs[i][1])
            continue
        else:
            # print("a[0]:", a[0], "减去same_pairs[i]:", same_pairs[i])
            a[0][1] = a[0][1] - int(same_pairs[i][1])
    a[0][1] = a[0][1] / k
    return a


#比较对的权重更新，如果最后更新完毕权重小于等于1，则从rowsortpairs中删除           
def deal_pairs(rowsortpairs):
    new_rowpairs = []  #不加权重的排序对
    new_pairadscore = []  #加权重的排序对
    #处理rowsortpairs，按照矛盾对进行权重更新，如果最后更新完毕权重小于等于1，则从rowsortpairs中删除
    #首先算权重加法，如果rowsortpairs中的元组有前两项相同的，就把第三项score的值加起来
    #然后做减法
    #在操作的过程中，要将处理到的相同和矛盾的元组从rowsortpairs中删除
    # for i in range(len(rowsortpairs)):
    #     new_rowpairs.append((rowsortpairs[i][0], rowsortpairs[i][1]))
    
    new_rowpairs = []  #去重

    # print("new_rowpairs:", new_rowpairs)
    # print("rowsortpairs:", list(rowsortpairs))
    
    #处理rowsortpairs,将每一个元组的进行拆分，前两项作为一个新的元组，例如（a,b,10）转变为[(a,b),10]
    for i in range(len(rowsortpairs)):
        # print("断点报错打印。。。。。。。。。。。。。。。。。。。。。。。。。:", rowsortpairs[i])
        new_rowpairs.append([(rowsortpairs[i][0], rowsortpairs[i][1]), rowsortpairs[i][2]])
    
    # print("new_rowpairs:", new_rowpairs)
    #中间储存pairs的列表，便于删除
    temp_list = new_rowpairs.copy()
    final_tuplepairs = []  #最终的排序对
    same_pairs = []  #相同的元组
    for i in range(len(new_rowpairs)):
        if new_rowpairs[i] not in temp_list:
            continue
        same_pairs = []
        same_pairs.append(new_rowpairs[i])
        # print("hahahah：", same_pairs)
        
        for j in range(i + 1, len(new_rowpairs)):
            if set(new_rowpairs[i][0]) == set(new_rowpairs[j][0]):
                same_pairs.append(new_rowpairs[j])
                if new_rowpairs[j] in temp_list:
                    temp_list.remove(new_rowpairs[j])
        if new_rowpairs[i] in temp_list:
            temp_list.remove(new_rowpairs[i])
            # print("temp_list:", temp_list)
        if len(same_pairs) == 1:  #并没有重复或矛盾的对
            final_tuplepairs.extend(same_pairs)
            # print("final_tuplepairs:", final_tuplepairs)
        elif len(same_pairs) > 1:  #有重复或矛盾的对
            
            final_tuplepairs.extend(deal_weight(same_pairs))  #进行权重的加减计算

        if len(same_pairs) == 0:
            break
        
    # print("final_tuplepairs:", final_tuplepairs)
    
    return final_tuplepairs  #列表


#比较对的权重更新，如果最后更新完毕权重小于等于1，则从rowsortpairs中删除           
def deal_final_pairs(new_rowpairs):
    # print("new_rowpairs,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:", len(new_rowpairs))
    # print("new_rowpairs,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:", new_rowpairs)
    # for k in range(len(new_rowpairs)):
    #     if k > 600:
    #         break
    #     print("new_rowpairs[k]:", new_rowpairs[k], k)
    #中间储存pairs的列表，便于删除
    temp_list = new_rowpairs.copy()
    final_tuplepairs = []  #最终的排序对
    same_pairs = []  #相同的元组
    for i in range(len(new_rowpairs)):
        if new_rowpairs[i] not in temp_list:
            continue
        same_pairs = []
        same_pairs.append(new_rowpairs[i])
        # print("奇怪爆发之前的new_rowpairs[i]:", new_rowpairs[i])
        for j in range(i + 1, len(new_rowpairs)):
            if set(new_rowpairs[i][0]) == set(new_rowpairs[j][0]):
                # print("奇怪爆发之前的new_rowpairs[j]:", new_rowpairs[j])
                same_pairs.append(new_rowpairs[j])
                if new_rowpairs[j] in temp_list:
                    temp_list.remove(new_rowpairs[j])
        if new_rowpairs[i] in temp_list:
            temp_list.remove(new_rowpairs[i])
        if len(same_pairs) == 1:  #并没有重复或矛盾的对
            final_tuplepairs.extend([same_pairs[0]])
        
        elif len(same_pairs) > 1:  #有重复或矛盾的对
            # print("奇怪爆发之前same_pairs:", same_pairs)
            final_tuplepairs.extend(deal_weight(same_pairs))  #进行权重的加减计算

        if len(same_pairs) == 0:
            break
        
    # print("final_tuplepairs:", final_tuplepairs)
    
    return final_tuplepairs  #列表


#按行读取csv文件，将每一行的第7、8、11、12列提取出来，然后调用extract_option_score函数，将选项和分数提取出来
#每一行按照矛盾原则，先整理一遍排序对，再加入大的排序对
def extract_option_score_from_csv(file_name):
    ALLsortpairs = []
    rowsortpairs = []
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        conut = 0
        for row in reader:
            # print("row:", row)
            choice1_before = row[5]  #正序的选项和分数
            choice2_before = row[7]  #逆序的选项和分数

            option1_before, score1_before = extract_option_score(choice1_before)
            
            option2_before, score2_before = extract_option_score(choice2_before)
            

            # print("option1_before:", option1_before, "score1_before:", score1_before)
            # print("option1_after:", option1_after, "score1_after:", score1_after)
            # print("option2_before:", option2_before, "score2_before:", score2_before)
            # print("option2_after:", option2_after, "score2_after:", score2_after)

            #利用每一个选项对应的道德原则和分数，构建一个排序对.flag=1表示正序，flag=-1表示逆序
            if int(score1_before) > 1:
                rowsortpairs.extend(rowsort_onechoice(option1_before, score1_before, row, 1))
            
            if int(score2_before) > 1:
                rowsortpairs.extend(rowsort_onechoice(option2_before, score2_before, row, -1))
            

            
            # if len(ALLsortpairs) > 534 and len(ALLsortpairs) < 552:
            #     print("rowsortpairs:", rowsortpairs)
            #     print("即将加入的列表", deal_pairs(rowsortpairs)) 
            ALLsortpairs.extend(deal_pairs(rowsortpairs)) #处理一行当中的排序对
            rowsortpairs = []  #清空rowsortpairs 
    print("*"*100)        
    # print(".....................................ALLsortpairs:", ALLsortpairs)
    print("*"*100)
    print("\n")
    
    Final_pairs = deal_final_pairs(ALLsortpairs)  #处理所有的排序对
    print(len(Final_pairs))
    #删除权重小于1的排序对
    box_pairs = []
    for i in range(len(Final_pairs)):
        try:
            if Final_pairs[i][1] >=  1:
                box_pairs.append(Final_pairs[i])
            elif Final_pairs[i][1] <= -1:
                box_pairs.append([(Final_pairs[i][0][1], Final_pairs[i][0][0]), -Final_pairs[i][1]])
        except:
            print("Final_pairs[i]:", Final_pairs[i])
        # if Final_pairs[i][1] >=  1:
        #     box_pairs.append(Final_pairs[i])
        # elif Final_pairs[i][1] <= -1:
        #     box_pairs.append([(Final_pairs[i][0][1], Final_pairs[i][0][0]), -Final_pairs[i][1]])
            
    print("...........................box_pairs.....................................\n:", box_pairs)

    return box_pairs


#根据索引表获得索引的排序对
def get_idexpairs(moral_pairs, moral_idx):
    idx_pairs = []
    print("moral_pairs:", moral_pairs)
    for i in range(len(moral_pairs)):
        idx_pairs.append((moral_idx[moral_pairs[i][0][0]], moral_idx[moral_pairs[i][0][1]]))
    print("idx_pairs:", idx_pairs)
    return idx_pairs




file_moralprinceple = './FF_data/moralprinciple.csv'
idx_moral, moral_idx = indxmoralprinciple(file_moralprinceple)  #加了索引的道德原则
print(idx_moral)
#将idx_moral写入csv文件,只在第一次运行的时候运行一次
# with open('./results_sort/moralprinciple_idx.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['idx', 'moralprinciple'])
#     for k,v in idx_moral.items():
#         writer.writerow([k+1, v])

# file_moraldilemma = './data/debatedata/dilemma_debate_chtogpt_ans.csv'##问题文件

file_moraldilemma = './FF_data/sex_nodebatedata/woman/dilemma_gemini_woman_ans.csv'##问题文件
file_results = './results_sort/sex_nodebate_results/rank_nodebate_gemini_woman.csv'
# text = "选项：B；；；坚定分数：2；；；；"
# print(extract_option_score(text))
moral_pairs = extract_option_score_from_csv(file_moraldilemma)  #从csv文件构建排序对

#根据索引表获得索引的排序对
idx_pairs = get_idexpairs(moral_pairs, moral_idx)

list_arrange_105 = ilsr_pairwise(184, idx_pairs, alpha=0.00001) #ilsr_pairwise函数的作用是对排序对进行处理，返回总体排序后的列表，8代表数据总条数，例如道德原则总数目

#这个alpha可以改，但是建议不改
#list_arrange_104 = ilsr_pairwise(780, my_list_new, alpha=0.0001) #780代表的是多少条要排序的东西
print("list_arrange_104", list_arrange_105)
print("np_shape", np.shape(list_arrange_105)) #输出排序后的列表的形状
DP = ranking_weights(list_arrange_105) #从0开始，需要+1,ranking weights函数作用是将排序后的列表转换成字典，key是idx，value是排序后的值，也就是权重
print("DP:", DP) #最终排序的索引和对应的权重
print('*' * 50)

#将索引对应的道德原则和权重写入新的csv文件

with open(file_results, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['idx', 'moralprinciple', 'weight'])
    for k,v in DP.items(): #将排序后的列表写入csv文件
        moralprinciple = idx_moral[k]
        writer.writerow([k+1, moralprinciple, v])


