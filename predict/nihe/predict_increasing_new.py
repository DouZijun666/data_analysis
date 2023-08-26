import json
import math

import matplotlib.pyplot as plt

# 原始数据
f = open("全国房地产开发投资增速new.txt", "r", encoding="UTF-8")
my_list = json.load(f)

x = []
y = []

for element in my_list:
    x.append(element["time"])
    y.append(element["percent"])

# y = 3.2475 + 10.2193*cos(x*0.2147) -3.6665*sin(x*0.2147) 傅里叶

# 新的数据点
new_x = ["1-8new", "1-9new", "1-10new", "1-11new", "1-12new"]
new_y = []

for i in range(13, 18):
    new_y.append(3.2475 + 10.2193 * math.cos(i * 0.2147) - 3.6665 * math.sin(i * 0.2147))

# 创建折线图
plt.plot(x, y, marker='o', label='Original Line')

# 在折线图上插入新点
plt.scatter(new_x, new_y, color='red', label='New Points')

# 添加标题和标签
plt.title('Line Chart with New Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 添加图例
plt.legend()

# 显示图形
plt.show()