# -*- coding: utf-8 -*-
import re
import pandas as pd

date_list = []
new_cases_list = []

for i in range(301, 327):
    date_list.append("0" + str(i))


def data_clean(filename, k):
    f = open("./Data/" + filename, 'r', encoding="utf-8")
    file = f.read()
    status = ["新增确诊病例", "新增出院病例", "新增死亡病例", "新增疑似病例"]
    new_cases_dict = {"日期": k}

    for j in status:
        new_cases = re.search(str(j) + r"(\d+)例", file).group(1)
        new_cases_dict[str(j)] = new_cases

    new_cases_list.append(new_cases_dict)

    f.close()


for i in date_list:
    data_clean(i + ".txt", i)

df = pd.DataFrame(new_cases_list)
print(df)

out_put_path = './病例.csv'
df.to_csv(out_put_path, sep=',', index=False, header=True, encoding="gbk")
