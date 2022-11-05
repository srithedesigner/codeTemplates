class Trie:

    def __init__(self):
        
        self.children = None
        self.isWord = False
    
    def add(self, word):
        
        node = self

        for char in word:
            
            if node.children[ord(char) - ord("a")]:
                node = node.children[ord(char) - ord("a")]
            else:
                node.children[ord(char) - ord("a")] = [Trie() for i in range(26)]
        
        node.isWord = True
    
    def search(self, word):

        node = self

        for char in word:
            
            if node.children[ord(char) - ord("a")]:
                node = node.children[ord(char) - ord("a")]
            else:
                return False
        
        if node.isWord:
            return True
    


        

