
class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
        
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next
    
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
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print( iter_node.get_item(), end= ' ')
            iter_node = iter_node.get_next()
        print()
        
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()
        
        

if __name__ == "__main__":
    q = Queue()
    q.insert(90)
    q.insert(20)
    q.insert(50)
    q.insert(80)
    q.insert(10)
    q.print()
    print( q.peak() )
    q.pop()
    q.print()
    print( q.peak() )
    
    
    
    
    