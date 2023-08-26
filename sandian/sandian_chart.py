"""
  散点图：
  横坐标：面积
  纵坐标：单位价格
"""
import json

import pyecharts.options as opts
from pyecharts.charts import Scatter

data = []

f = open("C:\\Users\\TY\\Desktop\\华为\\file_transform_file\\data.json", "r", encoding="UTF-8")
my_list = json.load(f)
f.close()

for element in my_list:
    data.append([element["area"], element["unit_price"]])
    # if isinstance(element["area"], float):
    #     print("True")
    # else:
    #     print("False")

# print(data)

data.sort(key=lambda x: x[0])
x_data = [d[0] for d in data]
y_data = [d[1] for d in data]

(
    Scatter()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts()
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="value", splitline_opts=opts.SplitLineOpts(is_show=True), name="area"
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
            name="unit_price"
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
        title_opts=opts.TitleOpts(title="area_unit_price散点图", pos_left="center", pos_bottom="1%"),
    )
    .render("sandian_chart.html")
)
