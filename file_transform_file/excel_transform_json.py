import xlrd, json


def read_xlsx_file(filename):
    # 打开Excel文件
    data = xlrd.open_workbook(filename)
    # 读取第一个工作表
    table = data.sheets()[0]
    # 统计行数
    rows = table.nrows
    data = []  # 存放数据
    for i in range(1, rows):
        values = table.row_values(i)
        data.append(
            (
                {
                    "title": str(values[0]),
                    "location": values[1],
                    "house_type": values[3],
                    "area": values[4],
                    "orientation": values[5],
                    "decoration": values[6],
                    "floor": values[7],
                    "structure": values[8],
                    "attention": values[9],
                    "release_time": values[10],
                    "total_price": values[11],
                    "unit_price": float(values[12].replace(",",""))
                }
            )
        )
    return data


if __name__ == '__main__':
    # d1 = read_xlsx_file("data.xlsx")
    d1 = read_xlsx_file("C:\\Users\\TY\\Desktop\\华为\\ciyun\\data(1).xlsx")
    # 字典中的数据都是单引号，但是标准的json需要双引号
    js = json.dumps(d1, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ':'))
    print(js)
    # 前面的数据只是数组，加上外面的json格式大括号
    js = "{" + js + "}"
    # 可读可写，如果不存在则创建，如果有内容则覆盖
    jsFile = open("./data1.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()