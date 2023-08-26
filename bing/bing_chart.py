"""
   饼图：
   展示二手房不同结构的数量
"""
import json

import pyecharts.options as opts
from pyecharts.charts import Pie


f = open("C:\\Users\\TY\\Desktop\\华为\\file_transform_file\\data.json", "r", encoding="UTF-8")
my_list = json.load(f)
f.close()

my_dict = {"板楼": 0, "板塔结合": 0, "平房": 0, "塔楼": 0, "暂无数据": 0}
x_data = []

for key in my_dict.keys():
    x_data.append(key)

for element in my_list:
    for key in my_dict.keys():
        if element["structure"].strip() == key:
            my_dict[key] += 1

y_data = []
for key in my_dict.keys():
    y_data.append(my_dict[key])

data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])

(
    Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
    .add(
        series_name="二手房数量",
        data_pair=data_pair,
        rosetype="radius",
        radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Customized Pie",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("bing_chart.html")
)