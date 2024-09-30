# 读取csv文件，新的四列，辩论前后选项是否会发生改变，以及坚定分数改变了多少（如果选项发生改变，则）
#新建的csv文件列名：moral_word, context, CA,CB,zh_choice_before, zh_score_before,zh_choice_after,zh_score_after,ni_choice_before,ni_score_before,ni_choice_after,ni_score_after,change_choice,change_score

import csv
import re


def deal_chosco(text):

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
        return option, int(score)
    elif matches1 and matches3:
        option = matches1[0]
        score = matches3[0]
        return option, int(score)
    elif matches4 and matches2:
        option = matches4[0]
        score = matches2[0]
        return option, int(score)
    elif matches4 and matches3:
        option = matches4[0]
        score = matches3[0]
        return option, int(score)
    else:
        print("pattern1", matches1)
        print("pattern2", matches2)
        print("pattern3", matches3)
        
        print("字符串未找到匹配的选项和分数")
        print("text:", text)
        return None, None
    return 1


def add_label(file_oo, file_new):

    with open(file_oo, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            zh_choice_before, zh_score_before = deal_chosco(row[6])
            zh_choice_after, zh_score_after = deal_chosco(row[7])
            ni_choice_before, ni_score_before = deal_chosco(row[10])
            ni_choice_after, ni_score_after = deal_chosco(row[11])
            if zh_choice_before != zh_choice_after:
                change_zh_choice = 1
            else:
                change_zh_choice = 0

            if ni_choice_before != ni_choice_after:
                change_ni_choice = 1
            else:
                change_ni_choice = 0
            # 如果发生改变，那就改变分数变成两者相加
            if change_zh_choice == 1:
                change_zh_score = -(zh_score_after + zh_score_before) #后面加上前面然后取负数
            else:
                change_zh_score = zh_score_after - zh_score_before

            if change_ni_choice == 1:
                change_ni_score = -(ni_score_after + ni_score_before)
            else:
                change_ni_score = ni_score_after - ni_score_before

            new_row = [row[0], row[1], row[2], row[3], zh_choice_before, zh_score_before, zh_choice_after, zh_score_after, change_zh_choice, change_zh_score, ni_choice_before, ni_score_before, ni_choice_after, ni_score_after, change_ni_choice, change_ni_score]
            with open(file_new, 'a', newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(new_row)
    print("Done")

if __name__ == '__main__':
    file_oo = "D:\VScode\lxl\Rankchoice\FF_data\debatedata\dilemma_debate_gpttogpt_ans.csv"
    file_new = "D:\VScode\lxl\Rankchoice\FF_data\debatedata_new\dilemma_debate_gpttogpt_ans_new.csv"
    add_label(file_oo, file_new)