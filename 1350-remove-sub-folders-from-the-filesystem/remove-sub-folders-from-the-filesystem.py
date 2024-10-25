class Trie:
    def __init__(self):
        self.children={}
        self.end_of_folder=False
    def add(self, folder):
        cur=self
        for f in folder.split("/"):
            if f not in cur.children:
                cur.children[f]= Trie()
            cur=cur.children[f]
        cur.end_of_folder=True
    def search_folder(self, folder):
        cur=self
        folders= folder.split("/")
        for i in range(len(folders)-1):
            cur=cur.children[folders[i]]
            if cur.end_of_folder:
                return False
        return True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie=Trie()
        for f in folder:
            trie.add(f)
        
        res=[]
        for f in folder:
            if trie.search_folder(f):
                res.append(f)
        return res