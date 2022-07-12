# -*- coding: utf-8 -*-
from Set import Set

if __name__ == "__main__":
    print('hii')
    s = Set()
    s.insert(32)
    s.insert(199)
    s.insert(50)
    s.insert(37)
    s.insert(199)
    s.insert(199)
    s.print()
    s.pop(199)
    s.print()
    s.insert(100)
    s.print()