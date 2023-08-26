"""
   演示pyecharts的基础入门
"""
import json

# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折线图对象
line = Line()
# 给折线图对象添加x轴的数据
f = open("C:\\Users\\TY\\Desktop\\华为\\file_transform_file\\data.json", "r", encoding="UTF-8")
my_list = json.load(f)
# print(my_list)
# print(type(my_list))
x_list: list[int] = []
y_list: list[int] = []
i = 1
for element in my_list:
    y_list.append(element["unit_price"])
    x_list.append(i)
    i += 1
line.add_xaxis(x_list)

# print(x_list)
# print(y_list)

# 给折线图对象添加y轴的数据
line.add_yaxis("unit_price", y_list)
# 设置全局配置项set_global_opts方法 pos = position
line.set_global_opts(
    title_opts=TitleOpts(title="unit_price_show", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=False)
)

# 通过render方法，将代码生成为图像
line.render("zhexian_chart.html")