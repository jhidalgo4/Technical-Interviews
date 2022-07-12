# -*- coding: utf-8 -*-

from Node import Node

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head == None
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            insertee = Node(new_item)
            self.tail.next = insertee
            self.tail = insertee
    
    def pop(self):
        if self.is_empty():
            return
        self.head = self.head.get_next()
        
    def print(self):
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end=' ')
            iter_node = iter_node.get_next()
        print()
    
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()