# -*- coding: utf-8 -*-

from LinkedList import LinkedList

if __name__ == "__main__":
    
    ll = LinkedList()
    ll.insert(40)
    ll.insert(69)
    ll.insert(37)
    ll.insert(100)
    ll.insert(21)
    ll.print()
    
    ll.remove(100)
    ll.print()
    
    ll.insert_after(21, 1)
    ll.print()
    
    ll.insert(99)
    ll.insert(30)
    ll.print()
    
    ll.remove(40)
    ll.print()
    
    ll.insert(77)
    ll.print()
    
    ll.remove_nth(7)
    ll.print()
    
    ll.insert(44)
    ll.print()
    
    ll.reverse()
    ll.print()
    
    ll.insert(77)
    ll.print()
    ll.remove_duplicates(77)
    ll.print()
    
    ll.remove(37)
    ll.print()
    ll.insert(88)
    ll.print()
