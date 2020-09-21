# -*- coding: utf-8 -*-
"""
@author lanqilu
@date Created in 2020/09/14  19:06
@file 04-广度优先搜索.py
@description 
"""
from collections import deque

graph = {"you": ["alice", "bob", "claire"],
         "alice": ["peggy"],
         "bob": ["anuj", "peggy"],
         "claire": ["thom", "jonny"],
         "anuj": [],
         "peggy": [],
         "thom": [],
         "jonny": []
         }


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    # 创建一个队列
    search_queue = deque()
    # 将“you”对应的value加入到对列中
    search_queue += graph[name]
    searched = []
    # 只要队列不为空
    while search_queue:
        # 取出第一个人
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
