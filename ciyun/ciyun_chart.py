"""
  词云图：
  统计热点词汇
"""

import pyecharts.options as opts
from pyecharts.charts import WordCloud

import json

# 将json文件转为列表
f = open("C:\\Users\\TY\\Desktop\\华为\\file_transform_file\\data.json", "r", encoding="UTF-8")
my_list: list[dict] = json.load(f)
f.close()
# print(my_dict)

# 计数容器
count_list: int = [0, 0, 0, 0, 0]
for element in my_list:
    if element["decoration"] == " 精装 ":
        count_list[0] += 1
    elif element["decoration"] == " 简装 ":
        count_list[1] += 1
    elif element["decoration"] == " 毛坯 ":
        count_list[2] += 1
    elif element["decoration"] == "装修":
        count_list[3] += 1
    else:
        count_list[4] += 1

# print(count_list)

my_dict = {"精装": count_list[0], "简装": count_list[1], "毛坯": count_list[2], "装修": count_list[3],
           "其他": count_list[4]}

data = []
for key in my_dict.keys():
    # print(key)
    my_tuple = (key, my_dict[key])
    data.append(my_tuple)

my_dict = {"1室1厅 ": 0, "1室2厅 ": 0, "2室1厅 ": 0, "2室2厅 ": 0, "3室1厅 ": 0, "3室2厅 ": 0, "3室3厅 ": 0,
           "4室1厅 ": 0,
           "4室2厅 ": 0, "4室3厅 ": 0, "5室1厅 ": 0, "5室2厅 ": 0, "5室3厅 ": 0, "5室4厅 ": 0, "6室1厅 ": 0,
           "6室2厅 ": 0,
           "6室3厅 ": 0, "6室4厅 ": 0, "7室2厅 ": 0, "8室2厅 ": 0, "9室3厅 ": 0}

# 二重循环减少代码量
for element in my_list:
    for key in my_dict:
        if element["house_type"] == key:
            my_dict[key] += 1

# print(my_dict)
for key in my_dict.keys():
    # print(key)
    my_tuple = (key, my_dict[key])
    data.append(my_tuple)

my_dict = {" 板楼": 0, " 板塔结合": 0, " 平房": 0, " 塔楼": 0, " 暂无数据": 0}

for element in my_list:
    for key in my_dict:
        if element["structure"] == key:
            my_dict[key] += 1

# print(my_dict)
for key in my_dict.keys():
    # print(key)
    my_tuple = (key, my_dict[key])
    data.append(my_tuple)

(
    WordCloud()
    .add(series_name="链家热点分析", data_pair=data, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="链家热点词汇词云图", title_textstyle_opts=opts.TextStyleOpts(font_size=25), pos_left="center", pos_bottom="1%"
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("ciyun_chart.html")
)