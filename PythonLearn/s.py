# -*- coding: utf-8 -*-
"""
@author lanqilu
@date Created in 2020/09/24  09:40
@file s.py
@description 
"""
import random

sumb = 0
sumg = 0

for i in range(1000000):
    a = random.randint(0, 1)
    if a == 1:
        sumb += 1
        continue
    else:
        while a == 0:
            sumg += 1
            a = random.randint(0, 1)
        sumb += 1
print(sumb)
print(sumg)
