from Stack import Stack

if __name__ == "__main__":
    print('hii')
    
    s = Stack()
    s.insert('1')
    s.insert('2100')
    s.insert('3700')
    s.insert('99')
    s.print()
    s.pop()
    s.print()
    s.insert('44')
    s.print()
    print(s.peak() )
    
    
    
    