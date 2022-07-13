
class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
        
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next
    
class Stack(object):
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
        else:
            insertee = Node(new_item, self.head)
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
            print(iter_node.get_item(), end= ' ' )
            iter_node = iter_node.get_next()
        print()
        
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()
        

if __name__ == "__main__":
    s = Stack()
    s.insert(31)
    s.insert(7)
    s.insert(81)
    s.insert(50)
    s.print()
    print( s.peak() )
    s.pop()
    s.print()
    print( s.peak() )