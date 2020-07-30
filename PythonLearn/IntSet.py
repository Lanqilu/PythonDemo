# -*- coding: utf-8 -*-
"""
@author lanqilu
@date Created in 2020/07/28  14:51
@file IntSet.py
@description 
"""


class IntSet(object):
    """IntSet是一个整数集合"""

    # 关于实现（不是抽象）的信息
    # 集合的值由一个整数数组self.Vals表示。
    # 集合中的每个整数在self.Vals中只出现一次。

    def __init__(self):
        """创建一个空的整数集合"""
        self.Vals = []

    def insert(self, e):
        """假设e是整数,将e插入搭self"""
        if e not in self.Vals:
            self.Vals.append(e)

    def member(self, e):
        """假设e是整数，\\
        如果e在self中，则返回True，否则返回False"""

        return e in self.Vals

    def remove(self, e):
        """假设e是整数，从self中删除e\\
           如果e不在self中，则抛出ValueError异常"""
        try:
            self.Vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def getMembers(self):
        """返回一个包含self中元素的列表\\
           对元素不进行排序"""
        return self.Vals[:]

    def __str__(self):
        """返回一个表示self的字符串"""
        self.Vals.sort()
        result = ''
        for e in self.Vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'  # -1 可以忽略最后的逗号


if __name__ == '__main__':
    s = IntSet()
    s.insert(3)
    s.insert(4)
    print(s)
