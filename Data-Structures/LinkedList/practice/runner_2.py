# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
        
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next
    

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def print(self):
        if self.isEmpty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end= ' ')
            iter_node = iter_node.get_next()
        print()
    
    def insert(self, new_item):
        if self.isEmpty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()
            
    def insertBegin(self, new_item):
        if self.isEmpty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            old_head = self.head
            insertee = Node(new_item, old_head)
            self.head = insertee
            
    def insertAfter(self, key, new_item):
        if self.isEmpty():
            return
        iter_node = self.head
        
        while iter_node:
            if iter_node.get_item() == key:
                break
            iter_node = iter_node.get_next()
        
        if iter_node.get_item() == key:
            insertee = Node(new_item, iter_node.get_next() )
            iter_node.next = insertee
            if iter_node.get_next() == None:
                self.tail = insertee
        
        
    def remove(self, key):
        if self.isEmpty():
            return
        
        if self.head.get_item() == key:
            self.head = self.head.get_next()
            return
        
        iter_node = self.head
        prev = None
        while iter_node:
            if iter_node.get_item() == key:
                prev.next = iter_node.get_next()
                if prev.get_next() == None:
                    self.tail = prev
                return
            prev = iter_node
            iter_node = iter_node.get_next()
            
            
    def removeNth(self, n):
        if self.isEmpty():
            return
        
        slow = self.head
        fast = slow
        
        for i in range(n):
            fast = fast.get_next()
            if i < n-1 and fast == None:
                return
        
        if fast == None:
            self.head = self.head.get_next()
            return
        
        while fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        
        next_node = slow.get_next().get_next()
        slow.next = next_node
        if next_node == None:
            self.tail = slow
            
            
    def reverse(self):
        if self.isEmpty() or self.head.get_next() == None:
            return
        
        iter_node = old_head = self.head
        prev = None
        while iter_node:
            next_node = iter_node.get_next()
            iter_node.next = prev
            prev = iter_node
            iter_node = next_node
        
        self.tail = old_head
        self.head = prev
        
        
    def remove_duplicates(self, key):
        if self.isEmpty() or self.head.get_next() == None:
            return
        
        iter_node = self.head
        prev = None
        while iter_node:
            if iter_node.get_item() == key:
                if prev == None:
                    self.head = self.head.get_next()
                    iter_node = iter_node.get_next()
                else:
                    next_node = iter_node.get_next()
                    prev.next = next_node
                    iter_node = next_node
                    if next_node == None:
                        self.tail = prev
                        return
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
                
    
    def get_intersect(self, list1, list2):
        len1 = len2 = 0
        p1 = list1.head
        p2 = list2.head
        
        while p1:
            p1 = p1.get_next()
            len1 += 1
        while p2:
            p2 = p2.get_next()
            len2 += 1
        
        p1 = list1.head
        p2 = list2.head
        
        for i in range(abs(len1-len2) ):
            if len1>len2:
                p1 = p1.get_next()
            else:
                p2 = p2.get_next()
        
        while p1.get_item() != p2.get_item():
            p1 = p1.get_next()
            p2 = p2.get_next()
            if p1 == None or p2 == None:
                return
            
        return p1.get_item()
    
    
    def hasCycle(self):
        if self.isEmpty() or self.head.get_next() == None:
            return False
        
        slow = fast = self.head
        
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                return True
        return False
    
    
    def beginCycle(self):
        if self.isEmpty() or self.head.get_next() == None:
            return
        slow = fast = self.head
        
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                break
        
        if slow == fast:
            slow = self.head
            while slow != fast:
                slow = slow.get_next()
                fast = fast.get_next()
            return slow.get_item()
        
        
    def odd_even_list(self):
        if self.isEmpty() or self.head.get_next() == None:
            return
        
        odd = self.head
        even = odd.get_next()
        even_head = even
        
        while even and odd and even.get_next() and odd.get_next():
            odd.next = even.get_next()
            odd = odd.get_next()
            even.next = odd.get_next()
            even = even.get_next()
        
        odd.next = even_head
        
        
    def is_palindrome(self):
        if self.isEmpty() or self.head.get_next():
            return True
        
        slow = fast = self.head
        
        while fast and fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        
        prev = None
        while slow:
            next_node = slow.get_next()
            slow.next = prev
            prev = slow
            slow = next_node
            
        
        left = self.head
        right = prev
        
        while right:
            if left.get_item() != right.get_item():
                return False
            left = left.get_next()
            right = right.get_next()
        
        return True
    
    
    
    def rotate_list(self, k):
        if self.isEmpty() or k == 0:
            return
        
        p1 = self.head
        len1 = 0
        while p1.get_next():
            len1+=1 
            p1 = p1.get_next()
        len1 += 1
        
        rotate = k % len1
        if rotate == 0:
            return
        
        p1.next = self.head
        p1 = self.head
        
        for i in range(len1 - k - 1):
            p1 = p1.get_next()
        
        next_node = p1.get_next()
        p1.next = None
        self.tail = p1
        self.head = next_node
        
        
    def add_two_nums(self, list1, list2):
        p1 = list1.head
        p2 = list2.head
        
        carry = 0
        holder = iter_node = Node(-1)
        
        while p1 or p2 or carry:
            v1 = v2 = 0
            
            if p1:
                v1 = p1.get_item()
                p1 = p1.get_next()
            
            if p2:
                v2 = p2.get_item()
                p2 = p2.get_next()
            
            v3 = v1+v2+carry
            iter_node.next = Node(v3%10)
            carry = v3 // 10
            iter_node = iter_node.get_next()
        
        return holder.get_next()
            
            
            
        
        
        
            
            
        
            
            
        
        
            
        
        
        
        
            
    
        
        
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(90)
    ll.insert(77)
    ll.insert(20)
    ll.insert(10)
    ll.insert(77)
    ll.print()
    # ll.insertBegin(11)
    # ll.print()
    ll.insertAfter(90, 93)
    ll.print()
    ll.insert(80)
    ll.print()
    ll.removeNth(4)
    ll.print()
    ll.remove(90)
    ll.print()
    ll.insert(96)
    ll.print()
    ll.reverse()
    ll.print()
    ll.insert(77)
    ll.print()
    ll.remove_duplicates(77)
    ll.print()
    
    
    
    
                
        
            
            
        
        