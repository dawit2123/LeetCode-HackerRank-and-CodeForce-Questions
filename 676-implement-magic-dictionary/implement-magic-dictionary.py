class Trie:
    def __init__(self):
        self.children={}
        self.word=False
class MagicDictionary:

    def __init__(self):
        self.root=Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur=self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c]=Trie()
                cur=cur.children[c]
            cur.word=True
        

    def search(self, searchWord: str) -> bool:
        def dfs(i, cur, max_replace):
            if max_replace<0:
                return False
            if i==(len(searchWord)):
                return cur.word and max_replace==0
            c=searchWord[i]   
            if c in cur.children:
                if dfs(i+1, cur.children[c], max_replace):
                    return True
            if max_replace>0:
                for char in cur.children:
                    if char!=c:
                        if dfs(i+1, cur.children[char], max_replace-1):
                            return True
            return False
        return dfs(0, self.root, 1)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)