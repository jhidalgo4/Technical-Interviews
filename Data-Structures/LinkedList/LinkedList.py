
from Node import Node

class LinkedList(object):
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
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()
            
    def insert_at_begin(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            old_head = self.head
            insertee = Node(new_item, old_head)
            self.head = insertee
            
    def insert_after(self, key, new_item):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            if iter_node.get_item() == key:
                insertee = Node(new_item )
                insertee.next = iter_node.get_next()
                if insertee.get_next() == None:
                    self.tail = insertee
                iter_node.next = insertee
                return
            iter_node = iter_node.get_next()
            
        
    
    def remove(self, key):
        if self.is_empty():
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
            
    
    def print(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end=' ' )
            iter_node = iter_node.get_next()
        print()
        
        
    def remove_nth(self, n):
        slow = self.head
        fast = slow
        for i in range(n):
            fast = fast.get_next()
            if fast == None and i < n-1:
                return
            
        if fast == None:
            self.head = self.head.get_next()
            return
        
        while fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next()
        
        next_node = slow.get_next().get_next()
        slow.next = next_node
        
        if next_node == None:
            self.tail = slow
            
    def reverse(self):
        old_head = self.head
        iter_node = old_head
        prev = None
        while iter_node:
            next_node = iter_node.get_next()
            iter_node.next = prev
            prev = iter_node
            iter_node = next_node
        self.head = prev
        self.tail = old_head
        
    
    def remove_duplicates(self, key):
        if self.is_empty():
            return
        iter_node = self.head
        prev = None
        while iter_node:
            if iter_node.get_item() == key:
                if prev == None:
                    self.head = self.head.get_next()
                    iter_node = iter_node.get_next()
                else:
                    prev.next = iter_node.get_next()
                    if prev.get_next() == None:
                        self.tail = prev
                    iter_node = iter_node.get_next()
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
        
    
    #given 2 linkedlist, find out where the linkedlist's begin to intersect
    #(overlap) ending the same way and return the point where they do
    def get_intersect(self, list1, list2):
        len1 = len2 = 0
        p1 = list1.head
        p2 = list2.head
        
        while p1:
            len1+= 1
            p1 = p1.get_next()
            
        while p2:
            len2+= 1
            p2 = p2.get_next()
        
        p1 = list1.head
        p2 = list2.head
        
        for i in range( abs(len1 - len2) ):
            if len1> len2:
                p1 = p1.get_next()
            else:
                p2 = p2.get_next()
            
        while p1.get_item() != p2.get_item():
            p1 = p1.get_next()
            p2 = p2.get_next()
            if p1 == None or p2 == None:
                return
        return p1.get_item()
    
    
    def has_cycle(self):
        if self.is_empty() or self.head.get_next() == None:
            return False
        slow = fast = self.head
        
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                return True
        return False
    
    
    def begin_of_cycle(self):
        if self.is_empty() or self.head.get_next() == None:
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
        
        return
        

    def even_odd_list(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        odd = self.head
        even = odd.get_next()
        even_head = even
        
        while even and odd and odd.get_next() and even.get_next():
            odd.next = even.get_next()
            odd = odd.get_next()
            even.next = odd.get_next()
            even = even.get_next()
        
        odd.next = even_head
        
        
    def is_palindrome(self):
        if self.is_empty() or self.head.get_next() == None:
            return True
        
        fast = slow = self.head
        
        #get slow iterator to be at the halfway mark
        while fast != None and fast.get_next() != None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
           
        #reverse the right-side of list to check for palindorme with left-side
        prev = None
        while slow != None:
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
        if self.head == None or self.head.get_next() == None or k == 0:
            return
        
        list_len = 0
        iter_node = self.head
        
        while iter_node.get_next():
            list_len += 1
            iter_node = iter_node.get_next()
        list_len += 1
        
        rotate_num = k % list_len
        
        if rotate_num == 0:
            return
        
        iter_node.next = self.head
        iter_node = self.head
        
        i = 0
        while i < list_len - rotate_num - 1:
            iter_node = iter_node.get_next()
            i += 1
        
        next_node = iter_node.get_next()
        iter_node.next = None
        self.tail = iter_node
        self.head = next_node
        
        
    
    def add_two_nums(self, list1, list2):
        carry = 0
        list1 = list1.head
        list2 = list2.head
        place_holder = iter_node = Node(-1)
        
        while list1 or list2 or carry:
            v1 = v2 = 0
            if list1:
                v1 = list1.get_item()
                list1 = list1.get_next()
            if list2:
                v2 = list2.get_item()
                list2 = list2.get_next()
                
            v3 = v1+v2 + carry
            iter_node.next = Node(v3%10)
            carry = v3 // 10
            iter_node = iter_node.get_next()
        
        return place_holder.get_next()
    
        
        
        
    
    

        
        
        
        
        
        
        
        
            