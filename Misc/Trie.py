class TrieNode(object):
    def __init__(self):
        self.end = False
        self.children = {}
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.root

        for letter in word:
            if letter not in temp.children:
                temp.children[letter] = TrieNode()
            temp = temp.children[letter]
        temp.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.root

        for letter in word:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        return temp.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.root

        for letter in prefix:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        return True