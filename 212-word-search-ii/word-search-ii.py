class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=False
    def add(self, word):
        curr=self
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.is_word=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for word in words:
            root.add(word)
        ROWS, COLS= len(board), len(board[0])
        result, path=set(),set()
        def dfs(r,c,node, word):
            if  (r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in path or board[r][c] not in node.children):
                return
            path.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.is_word:
                result.add(word)
            dfs(r+1,c,node, word)
            dfs(r-1,c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            path.remove((r,c))
        for R in range(ROWS):
            for C in range(COLS):
                dfs(R,C,root,"")
        return list(result)

        