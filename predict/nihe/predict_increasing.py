"""
  演示：预测全国房地产开发投资增速
"""

import json
import math

from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts

# 通过折线图展示已有数据

# 处理数据
f_us = open("全国房地产开发投资增速.txt", "r", encoding="UTF-8")
us_data = f_us.read()  # 美国的全部内容

# JSON转Python列表
us_list = json.loads(us_data)
# print(type(us_list))
# print(us_list)

x_list = []
y_list = []

for u_dict in us_list:
    x_list.append(u_dict["time"])
    y_list.append(u_dict["percent"])

# y = 3.2475 + 10.2193*cos(x*0.2147) -3.6665*sin(x*0.2147) 傅里叶
y_pre_list = []
for i in range(12, 17):
    y_pre = 3.2475 + 10.2193 * math.cos(i * 0.2147) - 3.6665 * math.sin(i * 0.2147)
    y_pre_list.append(y_pre)

x_pre_list = ["1-8月", "1-9月", "1-10月", "1-11月", "1-12月"]

for element in x_pre_list:
    x_list.append(element)

# for element in y_pre_list:
#     y_list.append(element)

line = Line()
line.add_xaxis(x_list)
line.add_yaxis("增速百分比", y_list, label_opts=LabelOpts(is_show=False))
# line.add_yaxis(x_pre_list)
line.add_yaxis("预测增速百分比", y_pre_list, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="全国房地产开发投资增速折线图", pos_left="center", pos_bottom="1%")
)

line.render("全国房地产开发投资增速折线图.html")

f_us.close()