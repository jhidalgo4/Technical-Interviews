
class Node(object):
    def __init__(self):
        self.children = {}
        self.is_leaf = False
        

class Trie(object):
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                iter_node.children[c] = Node()
            iter_node = iter_node.children[c]
        iter_node.is_leaf = True
    
    def search(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                return False
            iter_node = iter_node.children[c]
        
        if iter_node.is_leaf:
            return True
        return False
    
    def is_prefix(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                return False
            iter_node = iter_node.children[c]
        return True
        
    
    
if __name__ == "__main__":
    t = Trie()
    t.insert('soccer')
    t.insert('soap')
    t.insert('socal')
    
    print( t.search('socal') )
    print( t.is_prefix('sp') )
    print( t.is_prefix('so') )
    
    
        
        