import json
import csv
import os
# 打开原始文本文件和目标CSV文件
folder_path = './human_ann_ranking'
with open(os.path.join(folder_path,'json','ranking_alpha10-5.jsonl'), 'r') as file: #改这个中的最后一项文件名
    data = file.readlines()

with open(os.path.join(folder_path,'csv','ranking_alpha10-5.csv'), 'w', newline='') as file: #改这个中的最后一项文件名
    writer = csv.writer(file)

    # 写入CSV文件的标题行
    writer.writerow(['idx', 'nation', 'temperature', 'weight'])

    # 解析每一行JSON数据，并写入CSV文件
    for idx, line in enumerate(data):
        line = line.strip()
        if line:
            # 解析JSON数据
            json_data = json.loads(line)

            # 提取字段值
            nation = json_data['nation']
            temperature = json_data['temperature']
            weight = json_data['weight']

            # 写入CSV文件的一行数据
            writer.writerow([idx+1, nation, temperature, weight])


