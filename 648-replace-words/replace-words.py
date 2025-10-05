class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEndOfWord = True

    def search(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.isEndOfWord

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True

    def findShortedPrefix(self, word):
        curr = self.root
        for i, c in enumerate(word):
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return word
            curr = curr.children[index]
            if curr.isEndOfWord:
                return word[:i + 1]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        tokens = sentence.split()
        result = []
        for token in tokens:
            prefix = trie.findShortedPrefix(token)
            result.append(prefix)
        return ' '.join(result)