
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
            self.tail = self.tail.get_next()
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
                break
            iter_node = iter_node.get_next()
        
        if iter_node == None:
            return
        insertee = Node(new_item, iter_node.get_next() )
        iter_node.next = insertee
        if insertee.get_next() == None:
            self.tail = insertee
            
    
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
                next_node = iter_node.get_next()
                prev.next = next_node
                if next_node == None:
                    self.tail = prev
                return
            prev = iter_node
            iter_node = iter_node.get_next()
            
    def print(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end = ' ')
            iter_node = iter_node.get_next()
        print()
        
    
    def remove_nth(self, n):
        if self.is_empty():
            return
        
        slow = fast = self.head
        for i in range(n):
            fast = fast.get_next()
            if fast == None and i < n-1:
                return
        
        #removing the nth-0 item
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
        if self.is_empty() or self.head.get_next() == None:
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
        if self.is_empty() or self.head.get_next() == None:
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
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
        
    def get_intersect(self, list1, list2):
        len1 = len2 = 0
        list1 = list1.head
        list2 = list2.head
        
        while list1:
            len1+=1
            list1 = list1.get_next()
            
        while list2:
            len2 +=1
            list2 = list2.get_next()
        
        list1 = list1.head
        list2 = list2.head
        
        for i in range(len(len1-len2) ):
            if len1 > len2:
                list1 = list1.get_next()
            else:
                list2 = list2.get_next()
                
        while list1.get_item() != list2.get_item():
            list1.get_next()
            list2.get_next()
            if list1 == None or list2 == None:
                return
        
        return list1.get_item()
    
    def has_cycle(self):
        if self.is_empty() or self.get_next() == None:
            return False
        
        slow = fast = self.head
        
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                return True
        
        return False 
    
    
    def begin_cycle(self):
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
        
        while odd and even and even.get_next() and odd.get_next():
            odd.next = even.get_next()
            odd = odd.get_next()
            even.next = odd.get_next()
            even = even.get_next()
        
        odd.next = even_head
        
    def is_palindrome(self):
        if self.is_empty() or self.head.get_next() == None:
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
        
        while left and right:
            if left.get_item() != right.get_item():
                return False
            left = left.get_next()
            right = right.get_next()
        
        return True
    
    
    def rotate_list(self, k):
        if self.is_empty() or self.head.get_next() == None:
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
        
        for i in range(list_len - rotate_num - 1):
            iter_node = iter_node.get_next()
        
        next_node = iter_node.get_next()
        iter_node.next = None
        self.tail = iter_node
        self.head = next_node
    
    
    def add_two_nums(self, list1, list2):            
        p1 = list1.head
        p2 = list2.head
        
        carry = 0
        
        holder = iter_node = Node(-1)
        
        while carry or p1 or p2:
            v1 = v2 = 0
            if p1:
                v1 = p1.get_item()
                p1 = p1.get_next()
            
            if p2:
                v2 = p2.get_item()
                p2 = p2.get_next()
            
            v3 = v1 + v2 + carry
            iter_node.next = Node(v3 % 10)
            carry = v3 // 10
            iter_node = iter_node.get_next()
            
        return holder.get_next()
            
        
        
            
        
        
        
        
        


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(50)
    ll.insert(50)
    ll.insert(13)
    ll.insert(90)
    ll.print()
    ll.insert_at_begin(8)
    ll.print()
    ll.insert_after(50, 33)
    ll.print()
    ll.remove(33)
    ll.print()
    ll.insert(1)
    ll.insert(50)
    ll.print()
    ll.remove_nth(7)
    ll.print()
    ll.insert(50)
    ll.print()
    ll.remove_duplicates(50)
    ll.print()
    ll.insert(37)
    ll.print()
    
            
                
                
        
        
            
            
        
        
        