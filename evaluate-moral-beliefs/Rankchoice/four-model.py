import csv
#读取csv文件，计算四列都相同的数值3，2，1分的个数，以及平均值
file_oo = "D:\VScode\lxl\Rankchoice\FF_data\\four-model-choice.csv"
count_3 = 0
count_2 = 0
count_1 = 0


n_new_file_name = "D:\VScode\lxl\Rankchoice\FF_data\\nodebatedata\\M_four_ans.csv"
new_file_name = "D:\VScode\lxl\Rankchoice\FF_data\\nodebatedata\\NM_four_ans.csv"

##坚定不坚定
# with open(file_oo, 'r', encoding="gbk") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if row[4] != row[6] and int(row[5]) == 3:
#             #写入新文件
#             with open(new_file_name, 'a', newline='', encoding="utf-8") as f1:
#                 writer = csv.writer(f1)
#                 writer.writerow([row[8],row[9],row[10],row[11]])
#         if row[4] == row[6] or int(row[5]) == 1:
#             with open(n_new_file_name, 'a', newline='', encoding="utf-8") as f1:
#                 writer = csv.writer(f1)
#                 writer.writerow([row[8],row[9],row[10],row[11]])
        

#道德不道德
with open(file_oo, 'r', encoding="gbk") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == row[12] and row[2] == row[12] and row[4] == row[12] and row[6] == row[12]:
            #写入新文件
            with open(new_file_name, 'a', newline='', encoding="utf-8") as f1:
                writer = csv.writer(f1)
                writer.writerow([row[8],row[9],row[10],row[11]])
        if row[0] != row[12] and row[2] != row[12] and row[4] != row[12] and row[6] != row[12]:
            with open(n_new_file_name, 'a', newline='', encoding="utf-8") as f1:
                writer = csv.writer(f1)
                writer.writerow([row[8],row[9],row[10],row[11]])
        



                