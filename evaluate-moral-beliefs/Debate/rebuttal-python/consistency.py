#读取五个csv文件，计算每个文件中第六列。Kappa系数是评估分类数据的一致性，使用Karappa系数来评估五列数据的一致性。
import csv
import numpy as np
from sklearn.metrics import cohen_kappa_score
import sklearn

#计算两个list中的一致率
def conrate(list1, list2):
    n = len(list1)
    count = 0
    for i in range(n):
        if list1[i] == list2[i]:
            count += 1
    return count/n

#计算三个list中的一致率
def conrate_r(list1, list2,list3):
    n = len(list1)
    count = 0
    for i in range(n):
        if list1[i] == list2[i] and list2[i] == list3[i]:
            count += 1
    return count/n


def compute_kappa(file1_name, file2_name, file3_name, file4_name, file5_name):
    #读取五个csv文件,提取出每个文件中第六列作为一个数组
    file1 = open(file1_name, "r", encoding="gbk")
    reader1 = csv.reader(file1)
    A1 = []
    for item in reader1:
        if item[5] == "A":
            A1.append(0)
        else:
            A1.append(1)
    file1.close()

    file2 = open(file2_name, "r", encoding="gbk")
    reader2 = csv.reader(file2)
    A2 = []
    for item in reader2:
        if item[5] == "A":
            A2.append(0)
        else:
            A2.append(1)
    file2.close()

    file3 = open(file3_name, "r", encoding="gbk")
    reader3 = csv.reader(file3)
    A3 = []
    for item in reader3:
        if item[5] == "A":
            A3.append(0)
        else:
            A3.append(1)
    file3.close()

    file4 = open(file4_name, "r", encoding="gbk")
    reader4 = csv.reader(file4)
    A4 = []
    for item in reader4:
        if item[5] == "A":
            A4.append(0)
        else:
            A4.append(1)
    file4.close()

    file5 = open(file5_name, "r", encoding="gbk")
    reader5 = csv.reader(file5)
    A5 = []
    for item in reader5:
        if item[5] == "A":
            A5.append(0)
        else:
            A5.append(1)
    file5.close()

    #计算Kappa系数
    kappa = cohen_kappa_score(A1, A2)
    print("Kappa between file1 and file2: ", kappa, "Consistency rate: ", conrate(A1, A2))
    kappa = cohen_kappa_score(A1, A3)
    print("Kappa between file1 and file3: ", kappa, "Consistency rate: ", conrate(A1, A3))
    kappa = cohen_kappa_score(A1, A4)
    print("Kappa between file1 and file4: ", kappa, "Consistency rate: ", conrate(A1, A4))
    kappa = cohen_kappa_score(A1, A5)
    print("Kappa between file1 and file5: ", kappa, "Consistency rate: ", conrate(A1, A5))
    kappa = cohen_kappa_score(A2, A3)
    print("Kappa between file2 and file3: ", kappa, "Consistency rate: ", conrate(A2, A3))
    kappa = cohen_kappa_score(A2, A4)
    print("Kappa between file2 and file4: ", kappa, "Consistency rate: ", conrate(A2, A4))
    kappa = cohen_kappa_score(A2, A5)
    print("Kappa between file2 and file5: ", kappa, "Consistency rate: ", conrate(A2, A5))
    kappa = cohen_kappa_score(A3, A4)
    print("Kappa between file3 and file4: ", kappa, "Consistency rate: ", conrate(A3, A4))
    kappa = cohen_kappa_score(A3, A5)
    print("Kappa between file3 and file5: ", kappa, "Consistency rate: ", conrate(A3, A5))
    kappa = cohen_kappa_score(A4, A5)
    print("Kappa between file4 and file5: ", kappa, "Consistency rate: ", conrate(A4, A5))
    # print("Kappa between all files: ", cohen_kappa_score(A1, A2, A3, A4, A5))
    return 0

def compute_kappa_score(file1_name, file2_name, file3_name, file4_name, file5_name):
    #读取五个csv文件,提取出每个文件中第六列作为一个数组
    file1 = open(file1_name, "r", encoding="gbk")
    reader1 = csv.reader(file1)
    A1 = []
    for item in reader1:
        A1.append(int(item[6]))
    file1.close()

    file2 = open(file2_name, "r", encoding="gbk")
    reader2 = csv.reader(file2)
    A2 = []
    for item in reader2:
        A2.append(int(item[6]))
    file2.close()

    file3 = open(file3_name, "r", encoding="gbk")
    reader3 = csv.reader(file3)
    A3 = []
    for item in reader3:
        A3.append(int(item[6]))
    file3.close()

    file4 = open(file4_name, "r", encoding="gbk")
    reader4 = csv.reader(file4)
    A4 = []
    for item in reader4:
        A4.append(int(item[6]))
    file4.close()

    file5 = open(file5_name, "r", encoding="gbk")
    reader5 = csv.reader(file5)
    A5 = []
    for item in reader5:
        A5.append(int(item[6]))
    file5.close()

    #计算Kappa系数
    kappa = cohen_kappa_score(A1, A2)
    print("Kappa between file1 and file2: ", kappa, "Consistency rate: ", conrate(A1, A2))
    kappa = cohen_kappa_score(A1, A3)
    print("Kappa between file1 and file3: ", kappa, "Consistency rate: ", conrate(A1, A3))
    kappa = cohen_kappa_score(A1, A4)
    print("Kappa between file1 and file4: ", kappa, "Consistency rate: ", conrate(A1, A4))
    kappa = cohen_kappa_score(A1, A5)
    print("Kappa between file1 and file5: ", kappa, "Consistency rate: ", conrate(A1, A5))
    kappa = cohen_kappa_score(A2, A3)
    print("Kappa between file2 and file3: ", kappa, "Consistency rate: ", conrate(A2, A3))
    kappa = cohen_kappa_score(A2, A4)
    print("Kappa between file2 and file4: ", kappa, "Consistency rate: ", conrate(A2, A4))
    kappa = cohen_kappa_score(A2, A5)
    print("Kappa between file2 and file5: ", kappa, "Consistency rate: ", conrate(A2, A5))
    kappa = cohen_kappa_score(A3, A4)
    print("Kappa between file3 and file4: ", kappa, "Consistency rate: ", conrate(A3, A4))
    kappa = cohen_kappa_score(A3, A5)
    print("Kappa between file3 and file5: ", kappa, "Consistency rate: ", conrate(A3, A5))
    kappa = cohen_kappa_score(A4, A5)
    print("Kappa between file4 and file5: ", kappa, "Consistency rate: ", conrate(A4, A5))



def compute_kappa_r(file1_name, file2_name, file3_name):
    #读取五个csv文件,提取出每个文件中第六列作为一个数组
    file1 = open(file1_name, "r", encoding="gbk")
    reader1 = csv.reader(file1)
    A1 = []
    for item in reader1:
        if item[5] == "A":
            A1.append(0)
        else:
            A1.append(1)
    file1.close()

    file2 = open(file2_name, "r", encoding="gbk")
    reader2 = csv.reader(file2)
    A2 = []
    for item in reader2:
        if item[5] == "A":
            A2.append(0)
        else:
            A2.append(1)
    file2.close()

    file3 = open(file3_name, "r", encoding="gbk")
    reader3 = csv.reader(file3)
    A3 = []
    for item in reader3:
        if item[5] == "A":
            A3.append(0)
        else:
            A3.append(1)
    file3.close()

    

    #计算Kappa系数
    kappa = cohen_kappa_score(A1, A2)
    print("Kappa between file1 and file2: ", kappa, "Consistency rate: ", conrate(A1, A2))
    kappa = cohen_kappa_score(A1, A3)
    print("Kappa between file1 and file3: ", kappa, "Consistency rate: ", conrate(A1, A3))
   
    kappa = cohen_kappa_score(A2, A3)
    print("Kappa between file2 and file3: ", kappa, "Consistency rate: ", conrate(A2, A3))

    print("Consistency rate总: ", conrate_r(A1, A2, A3))
    
    # print("Kappa between all files: ", cohen_kappa_score(A1, A2, A3, A4, A5))
    return 0



def compute_kappa_score_r(file1_name, file2_name, file3_name):
    #读取五个csv文件,提取出每个文件中第六列作为一个数组
    file1 = open(file1_name, "r", encoding="gbk")
    reader1 = csv.reader(file1)
    A1 = []
    for item in reader1:
        A1.append(int(item[6]))
    file1.close()

    file2 = open(file2_name, "r", encoding="gbk")
    reader2 = csv.reader(file2)
    A2 = []
    for item in reader2:
        A2.append(int(item[6]))
    file2.close()

    file3 = open(file3_name, "r", encoding="gbk")
    reader3 = csv.reader(file3)
    A3 = []
    for item in reader3:
        A3.append(int(item[6]))
    file3.close()


    #计算Kappa系数
    kappa = cohen_kappa_score(A1, A2)
    print("Kappa between file1 and file2: ", kappa, "Consistency rate: ", conrate(A1, A2))
    kappa = cohen_kappa_score(A1, A3)
    print("Kappa between file1 and file3: ", kappa, "Consistency rate: ", conrate(A1, A3))
    
    kappa = cohen_kappa_score(A2, A3)
    print("Kappa between file2 and file3: ", kappa, "Consistency rate: ", conrate(A2, A3))

    print("Consistency rate总: ", conrate_r(A1, A2, A3))
   




#不同温度下
# file1_name = "D:\VScode\lxl\Debate\\rebuttal\\temperature-re\\t0_gemini_moralchoice.csv"
# file2_name = "D:\VScode\lxl\Debate\\rebuttal\\temperature-re\\t025_gemini_moralchoice.csv"
# file3_name = "D:\VScode\lxl\Debate\\rebuttal\\temperature-re\\t05_gemini_moralchoice.csv"
# file4_name = "D:\VScode\lxl\Debate\\rebuttal\\temperature-re\\t075_gemini_moralchoice.csv"
# file5_name = "D:\VScode\lxl\Debate\\rebuttal\\temperature-re\\t1_gemini_moralchoice.csv"
# compute_kappa_score(file1_name, file2_name, file3_name, file4_name, file5_name)
    

#多轮
file1_name = "D:\VScode\lxl\Debate\\rebuttal\\consistency-re\\r1_chatglm_moralchoice.csv"
file2_name = "D:\VScode\lxl\Debate\\rebuttal\\consistency-re\\r2_chatglm_moralchoice.csv"
file3_name = "D:\VScode\lxl\Debate\\rebuttal\\consistency-re\\r3_chatglm_moralchoice.csv"
compute_kappa_score_r(file1_name, file2_name, file3_name)
compute_kappa_r(file1_name, file2_name, file3_name)