class TrieNode(object):
    def __init__(self):
        self.end = False
        self.children = {}
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        temp = self.root

        for letter in word:
            if letter not in temp.children:
                temp.children[letter] = TrieNode()
            temp = temp.children[letter]
        temp.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(index, node):
            if index == len(word):
                return node.end
            if word[index] == '.':
                for child in node.children:
                    if dfs(index+1, node.children[child]):
                        return True
            if word[index] not in node.children:
                return False
            
            return dfs(index+1, node.children[word[index]])

        return dfs(0, self.root)

