# -*- coding: utf-8 -*-

class Set(object):
    def __init__(self):
        self.item = []
    
    def insert(self, new_item):
        for i in self.item:
            if i == new_item:
                return
        self.item.append(new_item)
        
    def pop(self, key):
        # for i in self.item:
        #     if i == key:
        #         self.item.remove(key)
        #         return
        for i in range(len(self.item) ):
            if self.item[i] == key:
                self.item.pop(i)
                return
                
    def print(self):
        print(self.item)
        
        