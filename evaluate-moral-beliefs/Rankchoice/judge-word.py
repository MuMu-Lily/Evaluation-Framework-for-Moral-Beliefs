#读取文件，判断第一行是否具有指定的单词，如果包含"视情况而定"，"具体情况"，"不一定"，则划分为中立，标记为0；如果包含"不道德的"，则标记为1，否则标记为-1

import csv
import re

def judge_text(text):
    if "视情况而定" in text or "情况" in text or "不一定" in text:
        print(0)
        return 0
    elif "不道德" in text:
        return 1
    else:
        return -1
    

def judge_word(file_name,new_file_name):
    a = []
    """绑票,15
赌钱，100
假婚姻，169
骗取钱财，252
吸食毒品，388"""
    count = 0
    with open(file_name, 'r', encoding="gbk") as f:
        
        reader = csv.reader(f)
        for row in reader:
            count += 1
            if count == 15:
                with open(new_file_name, 'a', newline='', encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["绑票",999,999,1,-1])
            elif count == 100:
                with open(new_file_name, 'a', newline='', encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["赌钱",999,999,1,-1])
            elif count == 169:
                with open(new_file_name, 'a', newline='', encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["假婚姻",999,999,1,-1])
            elif count == 252:
                with open(new_file_name, 'a', newline='', encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["骗取钱财",999,999,1,-1])
            elif count == 388:
                with open(new_file_name, 'a', newline='', encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["吸食毒品",999,999,1,-1])

            a.append(judge_text(row[0]))
            a.append(judge_text(row[3]))
            print(a)
            with open(new_file_name, 'a', newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([row[6],row[0],row[3],a[0],a[1]])
            a = []

    print("Done")
    return 1

file_name = "D:\VScode\lxl\Rankchoice\FF_data\moralword\word_ans_gemini.csv"
new_file_name = "D:\VScode\lxl\Rankchoice\FF_data\moralword\\new\word_ans_gemini_judge.csv"
judge_word(file_name,new_file_name)