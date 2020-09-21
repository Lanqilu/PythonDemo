# -*- coding: utf-8 -*-
"""
@author lanqilu
@date Created in 2020/09/14  18:23
@file 02-选择排序.py
@description 
"""


def findSmallest(arr):
    # 储存最小的值
    smallest = arr[0]
    # 储存最小元素的索引
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        # 将找出的最小的元素加入到新的数值中
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selectionSort([5, 3, 6, 2, 10]))
