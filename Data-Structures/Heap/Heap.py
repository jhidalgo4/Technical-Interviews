# -*- coding: utf-8 -*-

class Heap(object):
    def __init__(self):
        self.item = []
        self.size = 0
        
    def get_size(self):
        return self.size
        
    def display(self):
        print(self.item )
        
    def parent(self, index):
        if index == 0:
            return -1
        return (index - 1) // 2
    
    def left_child(self, index):
        result = (index*2) + 1
        if result >= self.get_size():
            return -1
        return result
    
    def right_chid(self, index):
        result = (index * 2) + 2
        if result >= self.get_size():
            return -1
        return result
        
    
    def insert(self, new_item):
        self.item.append(new_item)
        self.size = self.get_size() + 1
        index = self.get_size() - 1
        
        #Max Heap
        while index > 0 and new_item > self.item[self.parent(index)]:
            self.item[index] = self.item[self.parent(index)]
            index = self.parent(index)
        
        self.item[index] = new_item

        
    
    

    
        
        
        