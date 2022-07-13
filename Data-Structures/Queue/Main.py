# -*- coding: utf-8 -*-
from Queue import Queue

if __name__ == "__main__":
    
    q = Queue()
    q.insert(50)
    q.insert(100)
    q.insert(25)
    q.print()
    print( q.peak() )
    q.insert(75)
    q.insert(37)
    q.print()
    q.pop()
    q.print()
    print( q.peak() )
    
    
    