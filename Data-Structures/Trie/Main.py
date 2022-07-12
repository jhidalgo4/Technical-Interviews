from Trie import Trie

if __name__ == "__main__":
    t = Trie()
    t.insert('soccer')
    t.insert('soap')
    t.insert('water')
    t.insert('way')
    
    print(t.search_prefix("s"))
    print(t.search_prefix("waay"))
    print(t.search_prefix("wt"))


