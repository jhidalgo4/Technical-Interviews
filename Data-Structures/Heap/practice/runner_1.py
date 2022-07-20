# -*- coding: utf-8 -*-

class Heap(object):
    def __init__(self):
        self.item = []
        self.size = 0
        
    def getSize(self):
        return self.size
        
    def display(self):
        print(self.item)
        
    def parent(self, index):
        if index == 0:
            return -1
        return (index - 1) // 2
    
    def leftChild(self, index):
        result = (index * 2) + 1
        if result >= self.getSize():
            return -1
        return result
    
    def rightChild(self, index):
        result = (index * 2) + 2
        if result >= self.getSize():
            return -1
        return result
    
    def insert(self, newItem):
        self.item.append(newItem)
        self.size = self.getSize() + 1
        index = self.getSize() - 1
        
        while index > 0 and newItem > self.item[self.parent(index)]:
            self.item[index] = self.item[self.parent(index) ]
            index = self.parent(index)
        
        self.item[index] = newItem
        
        
        
    
    