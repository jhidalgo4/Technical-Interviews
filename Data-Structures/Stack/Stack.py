# -*- coding: utf-8 -*-

from Node import Node

class Stack(object):
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
        
    def insert(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            insertee = Node(item, self.head)
            self.head = insertee
    
    def pop(self):
        if self.is_empty():
            return
        self.head = self.head.get_next()
        
    def print(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end = ' ')
            iter_node = iter_node.get_next()
        print()
        
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()
        
        
        
    