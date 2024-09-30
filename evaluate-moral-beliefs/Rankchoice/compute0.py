#读取csv文件，计算为三分、为二分、一分的数据中选项发生改变的比例

import csv
import re


def count_j(file_name):
    count_3 = 0 #未发生改变的个数
    count_2 = 0
    count_1 = 0
    sum_3 = 0
    sum_2 = 0
    sum_1 = 0
    
    with open(file_name, 'r', encoding="gbk") as f:
        reader = csv.reader(f)
        for row in reader:
            if int(row[5]) == 1:
                sum_1 += 1
                if row[4] == row[6]:
                    count_1 += 1
            elif int(row[5]) == 2:
                sum_2 += 1
                if row[4] == row[6]:
                    count_2 += 1
            elif int(row[5]) == 3:
                sum_3 += 1
                if row[4] == row[6]:
                    count_3 += 1
            else:
                print("选项为空")
    
    if sum_3 == 0:
        sum_3 = 1
    if sum_2 == 0:
        sum_2 = 1
    if sum_1 == 0:
        sum_1 = 1
    print(count_3/sum_3)
    print(count_2/sum_2)
    print(count_1/sum_1)
    
    print("三分选项未发生改变的个数：", count_3)
    print("二分选项未发生改变的个数：", count_2)
    print("一分选项未发生改变的个数：", count_1)
    
    print("三分选项总个数：", sum_3)
    print("二分选项总个数：", sum_2)
    print("一分选项总个数：", sum_1)
    return count_3/sum_3, count_1/sum_1

file_name1 = "D:\VScode\lxl\Rankchoice\FF_data\debatedata_new\dilemma_debate_gpttoch_ans_new.csv"
file_name2 = "D:\VScode\lxl\Rankchoice\FF_data\debatedata_new\dilemma_debate_gpttoer_ans_new.csv"
file_name3 = "D:\VScode\lxl\Rankchoice\FF_data\debatedata_new\dilemma_debate_gpttoge_ans_new.csv"
file_name4 = "D:\VScode\lxl\Rankchoice\FF_data\debatedata_new\dilemma_debate_gpttogpt_ans_new.csv"

list_J = []
list_NJ = []
a,b = count_j(file_name1)
list_J.append(a)
list_NJ.append(b)
a,b = count_j(file_name2)
list_J.append(a)
list_NJ.append(b)
a,b = count_j(file_name3)
list_J.append(a)
list_NJ.append(b)
a,b = count_j(file_name4)
list_J.append(a)
list_NJ.append(b)
#求list_J和list_NJ的平均值
J = sum(list_J)/len(list_J)
NJ = sum(list_NJ)/len(list_NJ)
print(J)
print(NJ)