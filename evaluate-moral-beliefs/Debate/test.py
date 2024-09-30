import json


#按行读取json文件，并依次打印出来
def read(file_name):
    #打开json文件
    file = open(file_name, "r", encoding="utf-8")
    #按行读取json文件
    for line in file.readlines():
        #将json文件转化为字典
        dic = json.loads(line)
        #打印字典
        print(dic)
    
    return 1


file_name = "D:\VScode\lxl\Debate\\results\dilemma_debate_getoge_history.json"
read(file_name)