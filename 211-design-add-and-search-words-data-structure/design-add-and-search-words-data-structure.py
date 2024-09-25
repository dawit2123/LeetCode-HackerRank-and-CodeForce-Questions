class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.is_end_of_word=True
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur=root
            for i in range(j,len(word)):
                if word[i]==".":
                    for val in cur.children.values():
                        if dfs(i+1, val):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                    cur=cur.children[word[i]]
            return cur.is_end_of_word
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)