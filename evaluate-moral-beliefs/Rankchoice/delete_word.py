import csv


#写一个函数，读取csv文件，删除第一列中在给定列表当中的单词对应的行，并将结果写入新的csv文件。
def delete_word(file, new_file, word_list):
    # 读取csv文件
    with open(file, 'r', newline='', encoding='gbk') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] not in word_list:
                with open(new_file, 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)
    print('done')


def find_diff(file1, file2):
    lista = []
    with open(file1, 'r', newline='', encoding='utf-8') as f1:
        reader1 = csv.reader(f1)
        for row in reader1:
            print("row[6]", row)
            lista.append(row[0])

    with open(file2, 'r', newline='', encoding='utf-8') as f2:
        reader2 = csv.reader(f2)
        for row2 in reader2:
            if row2[6] not in lista:
                print(row2[6])
    print('done')
# 测试
# file1 = 'D:\VScode\lxl\Rankchoice\data\\nodebatedata\dilemma_chatglm_nodebate_answer.csv'
# new_file1 = 'D:\VScode\lxl\Rankchoice\FF_data\\nodebatedata\dilemma_chatglm_nodebate_answer.csv'

# file2 = 'D:\VScode\lxl\Rankchoice\data\\nodebatedata\dilemma_erine_nodebate_answer.csv'
# new_file2 = 'D:\VScode\lxl\Rankchoice\FF_data\\nodebatedata\dilemma_erine_nodebate_answer.csv'

# file3 = 'D:\VScode\lxl\Rankchoice\data\\nodebatedata\dilemma_gemini_nodebate_answer.csv'
# new_file3 = 'D:\VScode\lxl\Rankchoice\FF_data\\nodebatedata\dilemma_gemini_nodebate_answer.csv'

# file4 = 'D:\VScode\lxl\Rankchoice\data\\nodebatedata\dilemma_gpt35_nodebate_answer.csv'
# new_file4 = 'D:\VScode\lxl\Rankchoice\FF_data\\nodebatedata\dilemma_gpt35_nodebate_answer.csv'

# file1 = 'D:\VScode\lxl\Rankchoice\data\\debatedata\dilemma_debate_ertoch_ans.csv'
# new_file1 = 'D:\VScode\lxl\Rankchoice\FF_data\\debatedata\dilemma_debate_ertoch_ans.csv'

# file2 = 'D:\VScode\lxl\Rankchoice\data\\debatedata\dilemma_debate_ertoge_ans.csv'
# new_file2 = 'D:\VScode\lxl\Rankchoice\FF_data\\debatedata\dilemma_debate_ertoge_ans.csv'

# file3 = 'D:\VScode\lxl\Rankchoice\data\\debatedata\dilemma_debate_ertoer_ans.csv'
# new_file3 = 'D:\VScode\lxl\Rankchoice\FF_data\\debatedata\dilemma_debate_ertoer_ans.csv'

# file4 = 'D:\VScode\lxl\Rankchoice\data\\debatedata\dilemma_debate_ertogpt_ans.csv'
# new_file4 = 'D:\VScode\lxl\Rankchoice\FF_data\\debatedata\dilemma_debate_ertogpt_ans.csv'


# file1 = 'D:\VScode\lxl\Rankchoice\data\\sex_nodebatedata\woman\dilemma_chatglm_woman_ans.csv'
# new_file1 = 'D:\VScode\lxl\Rankchoice\FF_data\\sex_nodebatedata\woman\dilemma_chatglm_woman_ans.csv'

# file2 = 'D:\VScode\lxl\Rankchoice\data\\sex_nodebatedata\woman\dilemma_erine_woman_ans.csv'
# new_file2 = 'D:\VScode\lxl\Rankchoice\FF_data\\sex_nodebatedata\woman\dilemma_erine_woman_ans.csv'

# file3 = 'D:\VScode\lxl\Rankchoice\data\\sex_nodebatedata\woman\dilemma_gemini_woman_ans.csv'
# new_file3 = 'D:\VScode\lxl\Rankchoice\FF_data\\sex_nodebatedata\woman\dilemma_gemini_woman_ans.csv'

# file4 = 'D:\VScode\lxl\Rankchoice\data\\sex_nodebatedata\woman\dilemma_gpt_woman_ans.csv'
# new_file4 = 'D:\VScode\lxl\Rankchoice\FF_data\\sex_nodebatedata\woman\dilemma_gpt_woman_ans.csv'


file1 = "D:\VScode\lxl\Rankchoice\FF_data\moral-choice.csv"
new_file1 = 'D:\VScode\lxl\Rankchoice\FF_data\\moralword\moral-choice.csv'
# file2 = "D:\\VScode\\lxl\\Rankchoice\\FF_data\\nodebatedata\\dilemma_chatglm_nodebate_answer.csv"

"""word_list由以下词语构成：
吃着碗里瞧着锅里
出轨
出轨离婚
打骂孩子
 恶人先告状
 公报私仇
 婚后出轨
 借机报复
 狼狈为奸
 卖主求荣
 拈花惹草
 撒泼耍赖
 泄私愤
 以强凌弱
 以怨报德
 招妓
 争权夺利
 指桑骂槐
 捉奸在床
 追名逐利
 钻牛角尖
超速行驶
闯下大祸
吹牛拍马
吹牛皮
 哄抬
 挥霍
 脚踩两只船
 拉皮条
 轮奸
 谋私利
 曲意迎合
 杀夫
 擅离职守
 挖墙脚
 外遇
 性侵害
 移情别恋
 以私废公
 蝇营狗苟
 争名夺利"""
word_list = ['吃着碗里瞧着锅里','出轨','出轨离婚','打骂孩子','恶人先告状','公报私仇','婚后出轨','借机报复','狼狈为奸','卖主求荣','拈花惹草','撒泼耍赖','泄私愤','以强凌弱','以怨报德','招妓','争权夺利','指桑骂槐','捉奸在床','棒打鸳鸯','抓奸在床', '追名逐利','钻牛角尖','超速行驶','闯下大祸','吹牛拍马','吹牛皮','哄抬','挥霍','脚踩两只船','拉皮条','轮奸','谋私利','曲意迎合','杀夫','擅离职守','挖墙脚','外遇','性侵害','移情别恋','以私废公','蝇营狗苟','争名夺利']

delete_word(file1, new_file1, word_list)
# delete_word(file2, new_file2, word_list)
# delete_word(file3, new_file3, word_list)
# delete_word(file4, new_file4, word_list)

# file1 = 'D:\VScode\lxl\Rankchoice\FF_data\\nodebatedata\dilemma_chatglm_nodebate_answer.csv'
# file2 = "D:\VScode\lxl\Rankchoice\FF_data\\472基准文件.csv"
# find_diff(new_file4, file2)

# find_diff(file2, new_file4)
    