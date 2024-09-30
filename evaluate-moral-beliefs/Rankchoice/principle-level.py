import csv
#读取csv文件，储存为字典的列表
file_oo = "D:\VScode\lxl\Rankchoice\FF_data\principle-level.csv"
dic_list = []
dict0 = {}
i = 0
with open(file_oo, 'r', encoding="gbk") as f:
    reader = csv.reader(f)
    for row in reader:
        if i == 0:
            i = 1
            continue
        dict0[row[0]] = row[1]
print(dict0)

"""环保
道德规范
法律规定
可持续发展
社会公义
权益
尊重个人兴趣
尊重
透明
权利
"""
i = 1
l_a = []
file_name = "D:\VScode\lxl\Rankchoice\FF_data\\top10.csv"
with open(file_name, 'r', encoding="gbk") as f1:
    reader = csv.reader(f1)
    for row in reader:
        l_a.append(dict0[row[0]])
        if (i%10) == 0:
            print(l_a.count("2"),l_a.count("3"),l_a.count("4"),l_a.count("5"),l_a.count("6"))
            l_a = []
        i += 1

