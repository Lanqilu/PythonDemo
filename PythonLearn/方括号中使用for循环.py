# -*- coding: utf-8 -*-
"""
@author lanqilu
@date Created in 2020/07/30  09:06
@file 方括号中使用for循环.py
@description 
"""
# 传统写法
L1 = []
for i in range(1, 11):
    L1.append(i ** 2)
print("L1:\t" + str(L1))

# 列表解析：
L2 = [i ** 2 for i in range(1, 11)]
print("L2:\t" + str(L2))

# 传统写法

L3 = []
for i in range(1, 11):
    if i ** 2 > 50:
        L3.append(i ** 2)
print("L3:\t" + str(L3))

# 列表解析

L4 = [i ** 2 for i in range(1, 11) if i ** 2 > 50]
print("L4:\t" + str(L4))
