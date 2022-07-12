# -*- coding: utf-8 -*-


class Set(object):
    def __init__(self):
        self.item = []
    
    def insert(self, new_item):
        for i in self.item:
            if i == new_item:
                return
        self.item.append(new_item)
        
        # for i in range(len(self.item) ):
        #     if self.item[i] == new_item:
        #         return
        # self.item.append(new_item)
    
    def remove(self, key):
        for i in range(len(self.item) ):
            if self.item[i] == key:
                self.item.pop(i)
                return
            
    def print(self):
        print(self.item )
        
    

if __name__ == "__main__":
    
    s = Set()
    s.insert(90)
    s.insert(37)
    s.insert(8)
    s.insert(50)
    s.print()
    s.insert(25)
    s.print()
    s.remove(37)
    s.print()
        
    
    


