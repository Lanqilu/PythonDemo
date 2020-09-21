# -*- coding: utf-8 -*-
"""
@author lanqilu
@date Created in 2020/09/14  18:43
@file 03-快速排序.py
@description 
"""


def quicksort(array):
    if len(array) < 2:
        # 基线条件
        return array
    else:
        # 递归条件
        pivot = array[0]
        # 由所有小于基准值的元素组成的子数组
        less = [i for i in array[1:] if i <= pivot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3, 11]))
