# -*- coding: utf-8 -*-
"""
@author lanqilu
@date Created in 2020/07/30  08:50
@file 1.1一摞有序的纸牌.py
@description 
"""

import collections

# 用 collections.namedtuple 构建了一个简单的类来表示一张纸牌
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11) + list('JQKA')]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
