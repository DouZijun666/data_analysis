"""
   条形图：
   研究不同户型的精、简装修数量
"""
import json

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts

x_list = ["1室1厅 ", "1室2厅 ", "2室1厅 ", "2室2厅 ", "3室1厅 ", "3室2厅 ", "3室3厅 ", "4室1厅 ", "4室2厅 ", "4室3厅 ",
          "5室1厅 ", "5室2厅 ", "5室3厅 ", "5室4厅 ", "6室1厅 ", "6室2厅 ", "6室3厅 ", "6室4厅 ", "7室2厅 ", "8室2厅 ",
          "9室3厅 "]

my_dict = {}
for element in x_list:
    my_dict[element.strip()] = 0

# 将json文件转为列表
f = open("C:\\Users\\TY\\Desktop\\华为\\file_transform_file\\data.json", "r", encoding="UTF-8")
my_list: list[dict] = json.load(f)

# print(my_list)
# print(type(my_list))

for element in my_list:
    for list_element in x_list:
        if element["house_type"] == list_element:
            my_dict[list_element.strip()] += 1

# str：户型 list[精装, 简装, 毛坯]
y_dict: dict[str: list[int, int, int]] = {}

for element in my_dict.keys():
    y_dict[element] = [0, 0, 0, 0]
    # error
    # y_dict[element][0] = 0
    # y_dict[element][1] = 0
    # y_dict[element][2] = 0

# print(y_dict)

for element in my_list:
    for key_element in my_dict.keys():
        if element["decoration"] == " 精装 " and element["house_type"] == key_element + " ":
            y_dict[key_element][0] += 1
        elif element["decoration"] == " 简装 " and element["house_type"] == key_element + " ":
            y_dict[key_element][1] += 1
        elif element["decoration"] == " 毛坯 " and element["house_type"] == key_element + " ":
            y_dict[key_element][2] += 1
for element in my_dict.keys():
    y_dict[element][3] = y_dict[element][0] + y_dict[element][1] + y_dict[element][2]

# print(my_dict)
# print(y_dict)
# print(y_dict[x_list[0].strip()][0] / y_dict[x_list[0].strip()][3])

y_list1 = [
    {"value": y_dict[x_list[0].strip()][0], "percent": y_dict[x_list[0].strip()][0] / y_dict[x_list[0].strip()][3]},
    {"value": y_dict[x_list[1].strip()][0], "percent": y_dict[x_list[1].strip()][0] / y_dict[x_list[1].strip()][3]},
    {"value": y_dict[x_list[2].strip()][0], "percent": y_dict[x_list[2].strip()][0] / y_dict[x_list[2].strip()][3]},
    {"value": y_dict[x_list[3].strip()][0], "percent": y_dict[x_list[3].strip()][0] / y_dict[x_list[3].strip()][3]},
    {"value": y_dict[x_list[4].strip()][0], "percent": y_dict[x_list[4].strip()][0] / y_dict[x_list[4].strip()][3]},
    {"value": y_dict[x_list[5].strip()][0], "percent": y_dict[x_list[5].strip()][0] / y_dict[x_list[5].strip()][3]},
    {"value": y_dict[x_list[6].strip()][0], "percent": y_dict[x_list[6].strip()][0] / y_dict[x_list[6].strip()][3]},
    {"value": y_dict[x_list[7].strip()][0], "percent": y_dict[x_list[7].strip()][0] / y_dict[x_list[7].strip()][3]},
    {"value": y_dict[x_list[8].strip()][0], "percent": y_dict[x_list[8].strip()][0] / y_dict[x_list[8].strip()][3]},
    {"value": y_dict[x_list[9].strip()][0], "percent": y_dict[x_list[9].strip()][0] / y_dict[x_list[9].strip()][3]},
    {"value": y_dict[x_list[10].strip()][0], "percent": y_dict[x_list[10].strip()][0] / y_dict[x_list[10].strip()][3]},
    {"value": y_dict[x_list[11].strip()][0], "percent": y_dict[x_list[11].strip()][0] / y_dict[x_list[11].strip()][3]},
    {"value": y_dict[x_list[12].strip()][0], "percent": y_dict[x_list[12].strip()][0] / y_dict[x_list[12].strip()][3]},
    {"value": y_dict[x_list[13].strip()][0], "percent": y_dict[x_list[13].strip()][0] / y_dict[x_list[13].strip()][3]},
    {"value": y_dict[x_list[14].strip()][0], "percent": y_dict[x_list[14].strip()][0] / y_dict[x_list[14].strip()][3]},
    {"value": y_dict[x_list[15].strip()][0], "percent": y_dict[x_list[15].strip()][0] / y_dict[x_list[15].strip()][3]},
    {"value": y_dict[x_list[16].strip()][0], "percent": y_dict[x_list[16].strip()][0] / y_dict[x_list[16].strip()][3]},
    {"value": y_dict[x_list[17].strip()][0], "percent": y_dict[x_list[17].strip()][0] / y_dict[x_list[17].strip()][3]},
    {"value": y_dict[x_list[18].strip()][0], "percent": y_dict[x_list[18].strip()][0] / y_dict[x_list[18].strip()][3]},
    {"value": y_dict[x_list[19].strip()][0], "percent": y_dict[x_list[19].strip()][0] / y_dict[x_list[19].strip()][3]},
    {"value": y_dict[x_list[20].strip()][0], "percent": y_dict[x_list[20].strip()][0] / y_dict[x_list[20].strip()][3]}
]

y_list2 = [
    {"value": y_dict[x_list[0].strip()][1], "percent": y_dict[x_list[0].strip()][1] / y_dict[x_list[0].strip()][3]},
    {"value": y_dict[x_list[1].strip()][1], "percent": y_dict[x_list[1].strip()][1] / y_dict[x_list[1].strip()][3]},
    {"value": y_dict[x_list[2].strip()][1], "percent": y_dict[x_list[2].strip()][1] / y_dict[x_list[2].strip()][3]},
    {"value": y_dict[x_list[3].strip()][1], "percent": y_dict[x_list[3].strip()][1] / y_dict[x_list[3].strip()][3]},
    {"value": y_dict[x_list[4].strip()][1], "percent": y_dict[x_list[4].strip()][1] / y_dict[x_list[4].strip()][3]},
    {"value": y_dict[x_list[5].strip()][1], "percent": y_dict[x_list[5].strip()][1] / y_dict[x_list[5].strip()][3]},
    {"value": y_dict[x_list[6].strip()][1], "percent": y_dict[x_list[6].strip()][1] / y_dict[x_list[6].strip()][3]},
    {"value": y_dict[x_list[7].strip()][1], "percent": y_dict[x_list[7].strip()][1] / y_dict[x_list[7].strip()][3]},
    {"value": y_dict[x_list[8].strip()][1], "percent": y_dict[x_list[8].strip()][1] / y_dict[x_list[8].strip()][3]},
    {"value": y_dict[x_list[9].strip()][1], "percent": y_dict[x_list[9].strip()][1] / y_dict[x_list[9].strip()][3]},
    {"value": y_dict[x_list[10].strip()][1], "percent": y_dict[x_list[10].strip()][1] / y_dict[x_list[10].strip()][3]},
    {"value": y_dict[x_list[11].strip()][1], "percent": y_dict[x_list[11].strip()][1] / y_dict[x_list[11].strip()][3]},
    {"value": y_dict[x_list[12].strip()][1], "percent": y_dict[x_list[12].strip()][1] / y_dict[x_list[12].strip()][3]},
    {"value": y_dict[x_list[13].strip()][1], "percent": y_dict[x_list[13].strip()][1] / y_dict[x_list[13].strip()][3]},
    {"value": y_dict[x_list[14].strip()][1], "percent": y_dict[x_list[14].strip()][1] / y_dict[x_list[14].strip()][3]},
    {"value": y_dict[x_list[15].strip()][1], "percent": y_dict[x_list[15].strip()][1] / y_dict[x_list[15].strip()][3]},
    {"value": y_dict[x_list[16].strip()][1], "percent": y_dict[x_list[16].strip()][1] / y_dict[x_list[16].strip()][3]},
    {"value": y_dict[x_list[17].strip()][1], "percent": y_dict[x_list[17].strip()][1] / y_dict[x_list[17].strip()][3]},
    {"value": y_dict[x_list[18].strip()][1], "percent": y_dict[x_list[18].strip()][1] / y_dict[x_list[18].strip()][3]},
    {"value": y_dict[x_list[19].strip()][1], "percent": y_dict[x_list[19].strip()][1] / y_dict[x_list[19].strip()][3]},
    {"value": y_dict[x_list[20].strip()][1], "percent": y_dict[x_list[20].strip()][1] / y_dict[x_list[20].strip()][3]}
]

y_list3 = [
    {"value": y_dict[x_list[0].strip()][2], "percent": y_dict[x_list[0].strip()][2] / y_dict[x_list[0].strip()][3]},
    {"value": y_dict[x_list[1].strip()][2], "percent": y_dict[x_list[1].strip()][2] / y_dict[x_list[1].strip()][3]},
    {"value": y_dict[x_list[2].strip()][2], "percent": y_dict[x_list[2].strip()][2] / y_dict[x_list[2].strip()][3]},
    {"value": y_dict[x_list[3].strip()][2], "percent": y_dict[x_list[3].strip()][2] / y_dict[x_list[3].strip()][3]},
    {"value": y_dict[x_list[4].strip()][2], "percent": y_dict[x_list[4].strip()][2] / y_dict[x_list[4].strip()][3]},
    {"value": y_dict[x_list[5].strip()][2], "percent": y_dict[x_list[5].strip()][2] / y_dict[x_list[5].strip()][3]},
    {"value": y_dict[x_list[6].strip()][2], "percent": y_dict[x_list[6].strip()][2] / y_dict[x_list[6].strip()][3]},
    {"value": y_dict[x_list[7].strip()][2], "percent": y_dict[x_list[7].strip()][2] / y_dict[x_list[7].strip()][3]},
    {"value": y_dict[x_list[8].strip()][2], "percent": y_dict[x_list[8].strip()][2] / y_dict[x_list[8].strip()][3]},
    {"value": y_dict[x_list[9].strip()][2], "percent": y_dict[x_list[9].strip()][2] / y_dict[x_list[9].strip()][3]},
    {"value": y_dict[x_list[10].strip()][2], "percent": y_dict[x_list[10].strip()][2] / y_dict[x_list[10].strip()][3]},
    {"value": y_dict[x_list[11].strip()][2], "percent": y_dict[x_list[11].strip()][2] / y_dict[x_list[11].strip()][3]},
    {"value": y_dict[x_list[12].strip()][2], "percent": y_dict[x_list[12].strip()][2] / y_dict[x_list[12].strip()][3]},
    {"value": y_dict[x_list[13].strip()][2], "percent": y_dict[x_list[13].strip()][2] / y_dict[x_list[13].strip()][3]},
    {"value": y_dict[x_list[14].strip()][2], "percent": y_dict[x_list[14].strip()][2] / y_dict[x_list[14].strip()][3]},
    {"value": y_dict[x_list[15].strip()][2], "percent": y_dict[x_list[15].strip()][2] / y_dict[x_list[15].strip()][3]},
    {"value": y_dict[x_list[16].strip()][2], "percent": y_dict[x_list[16].strip()][2] / y_dict[x_list[16].strip()][3]},
    {"value": y_dict[x_list[17].strip()][2], "percent": y_dict[x_list[17].strip()][2] / y_dict[x_list[17].strip()][3]},
    {"value": y_dict[x_list[18].strip()][2], "percent": y_dict[x_list[18].strip()][2] / y_dict[x_list[18].strip()][3]},
    {"value": y_dict[x_list[19].strip()][2], "percent": y_dict[x_list[19].strip()][2] / y_dict[x_list[19].strip()][3]},
    {"value": y_dict[x_list[20].strip()][2], "percent": y_dict[x_list[20].strip()][2] / y_dict[x_list[20].strip()][3]}
]
c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1500px", height="1000px"))
    .add_xaxis(x_list)
    .add_yaxis("精装", y_list1, stack=True, category_gap="50%", label_opts=LabelOpts(is_show=False))
    .add_yaxis("简装", y_list2, stack=True, category_gap="50%", label_opts=LabelOpts(is_show=False))
    .add_yaxis("毛坯", y_list3, stack=True, category_gap="50%", label_opts=LabelOpts(is_show=False))

    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
        )
    )

    .set_global_opts(
        title_opts=TitleOpts(title="不同户型的精简装修数据分析", pos_left="center", pos_bottom="1%")
    )
    .render("bar_chart.html")
)