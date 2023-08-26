"""
  通过回归模型进行房价的预测
"""
import json

# y = 9.297371 * x - 549.1166  回归
import matplotlib.pyplot as plt


f = open("C:\\Users\\TY\\Desktop\\华为\\file_transform_file\\data.json", "r", encoding="UTF-8")
x = []
my_list = json.load(f)
for element in my_list:
    x.append(element["area"])
f.close()

# print(x)

# 绘制直线图
y = []
for element in x:
    y.append(9.297371 * element - 549.1166)

plt.plot(x, y, label='regression_curve', color='blue')

# 添加散点
z = []
for element in my_list:
    z.append(element["total_price"])
scatter_x = x
scatter_y = z
plt.scatter(scatter_x, scatter_y, color='red', label='true_dot')

# 添加标题和标签
plt.title('regression_model')
plt.xlabel('area')
plt.ylabel('total_price')

# 添加图例
plt.legend()

# 显示图形
plt.show()
