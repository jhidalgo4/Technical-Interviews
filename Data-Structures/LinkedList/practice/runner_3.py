class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
        
    def getNext(self):
        return self.next
    
    def getItem(self):
        return self.item
    

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def insert(self, newItem):
        if self.isEmpty():
            self.head = Node(newItem)
            self.tail = self.head
        else:
            self.tail.next = Node(newItem)
            self.tail = self.tail.getNext()
    
    def insertAtBegin(self, newItem):
        if self.isEmpty():
            self.head = Node(newItem)
            self.tail = self.head
        else:
            oldHead = self.head
            insertee = Node(newItem, oldHead)
            self.head = insertee
            
    def insertAfter(self, key, newItem):
        if self.isEmpty():
            return
        iterNode = self.head
        while iterNode:
            if iterNode.getItem() == key:
                nextNode = iterNode.getNext()
                insertee = Node(newItem, nextNode)
                iterNode.next = insertee
                if nextNode == None:
                    self.tail = insertee
            iterNode = iterNode.getNext()
            
    def remove(self, key):
        if self.isEmpty():
            return
        if self.head.getItem() == key:
            self.head = self.head.getNext()
            return
        iterNode = self.head
        prev = None
        while iterNode:
            if iterNode.getItem() == key:
                nextNode = iterNode.getNext()
                prev.next = nextNode
                if nextNode == None:
                    self.tail = prev
                return
            prev = iterNode
            iterNode = iterNode.getNext()
            
    def removeDuplicates(self, key):
        if self.isEmpty():
            return
        iterNode = self.head
        prev = None
        
        while iterNode:
            if iterNode.getItem() == key:
                if prev == None:
                    self.head = self.head.getNext()
                    iterNode = iterNode.getNext()
                else:
                    nextNode = iterNode.getNext()
                    prev.next = nextNode
                    if nextNode == None:
                        self.tail = prev
                        return
            else:
                prev = iterNode 
                iterNode = iterNode.getNext()
    
    
    def removeNth(self, n):
        slow = fast = self.head
        for i in range(n):
            fast = fast.getNext()
            if fast == None and i<n-1:
                return
            
        if fast == None:
            self.head = self.head.getNext()
            return
        
        while fast.getNext():
            fast = fast.getNext()
            slow = slow.getNext()
        
        nextNode = slow.getNext().getNext()
        slow.next = nextNode
        
        if nextNode == None:
            self.tail = slow
            
    
    def reverse(self):
        if self.isEmpty() or self.head.getNext() == None:
            return
        iterNode = oldHead = self.head
        prev = None
        
        while iterNode:
            nextNode = iterNode.getNext()
            iterNode.next = prev
            prev = iterNode
            iterNode = nextNode
        
        self.head = prev
        self.tail = oldHead
        
    
    def getIntersect(self, list1, list2):
        len1 = len2 = 0
        p1 = list1.head
        p2 = list2.head
        
        while p1:
            len1+=1
            p1 = p1.getNext()
        
        while p2:
            len2 += 1
            p2 = p2.getNext()
        
        p1 = list1.head
        p2 = list2.head
        
        for i in range(abs(len1-len2) ):
            if len1 > len2:
                p1 = p1.getNext()
            else:
                p2 = p2.getNext()
            
        while p1.getItem() != p2.getItem():
            p1 = p1.getNext()
            p2 = p2.getNext()
            if p1 == None or p2 == None:
                return
        return p1.getItem()
    
    def hasCycle(self):
        if self.isEmpty() or self.head.getNext() == None:
            return False
        
        slow = fast = self.head
        
        while fast.getNext() and fast.getNext().getNext():
            slow = slow.getNext()
            fast = fast.getNext().getNext()
            if slow == fast:
                return True
            
        return False
    
    def beginCycle(self):
        if self.isEmpty() or self.head.getNext() == None:
            return 
        
        slow = fast = self.head
        
        while fast.getNext() and fast.getNext().getNext():
            slow = slow.getNext()
            fast = fast.getNext().getNext()
            if slow == fast:
                break
        
        if slow == fast:
            slow = self.head
            while slow != fast:
                slow = slow.getNext()
                fast = fast.getNext()
            return slow.getItem()
    
    def OddEvenList(self):
        odd = self.head
        even = odd.getNext()
        evenHead = even
        
        while odd and even and odd.getNext() and even.getNext():
            odd.next = even.getNext()
            odd = odd.getNext()
            even.next = odd.getNext()
            even = even.getNext()
            
        odd.next = evenHead
        
    
    def isPalindrome(self):
        if self.isEmpty() or self.head.getNext() == None:
            return True
        
        slow = fast = self.head
        
        while fast and fast.getNext():
            fast = fast.getNext().getNext()
            slow = slow.getNext()
            
        prev = None
        
        while slow:
            nextNode = slow.getNext()
            slow.next = prev
            prev = slow
            slow = nextNode
            
        left = self.head
        right = prev
        
        while right:
            if left.getItem() != right.getItem():
                return False
            left = left.getNext()
            right = right.getNext()
        
        return True
    
    
    def rotateList(self, n):
        if self.isEmpty() or self.head.getNext() == None or n == 0:
            return
        
        iterNode = self.head
        len1 = 0
        while iterNode.getNext():
            len1 += 1
            iterNode = iterNode.getNext()
        len1 += 1
        
        rotate = n % len1
        if rotate == 0:
            return
        
        iterNode.next = self.head
        iterNode = self.head
        
        for i in range(len1 - rotate - 1):
            iterNode = iterNode.getNext()
        
        nextNode = iterNode.getNext()
        iterNode.next = None
        self.head = nextNode
        self.tail = iterNode
    
    
    def addList(self, list1, list2):
        l1 = list1.head
        l2 = list2.head
        carry = 0
        holder = iterNode = Node(-1)
        
        while l1 or l2 or carry:
            v1 = v2 = 0
            
            if l1:
                v1 = l1.getItem()
                l1 = l1.getNext()
            
            if l2:
                v2 = l2.getItem()
                l2 = l2.getNext()
            
            v3 = v1+v2+carry
            iterNode.next = Node(v3 % 10)
            carry = v3 // 10
            iterNode = iterNode.getNext()
        
        return holder.getNext()
            
                
                
        
    def display(self):
        if self.isEmpty():
            return
        iterNode = self.head
        while iterNode:
            print(iterNode.getItem(), end = ' ')
            iterNode = iterNode.getNext()
        print()


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBegin(10)
    ll.insert(50)
    ll.insertAtBegin(70)
    ll.insert(40)
    ll.insert(90)
    ll.insert(20)
    ll.insertAfter(90, 93)
    ll.insert(80)
    
    ll.display()
    ll.remove(50)
    ll.insert(30)
    ll.display()
    ll.reverse()
    ll.display()
    
    
            
            
            