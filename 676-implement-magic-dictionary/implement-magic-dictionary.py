from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.is_end_of_word = True

    def search(self, searchWord: str) -> bool:
        def dfs(node, index, changes_allowed):
            if changes_allowed < 0:
                return False
            
            if index == len(searchWord):
                return node.is_end_of_word and changes_allowed == 0

            char_to_match = searchWord[index]

            # Try to match the character directly
            if char_to_match in node.children:
                if dfs(node.children[char_to_match], index + 1, changes_allowed):
                    return True

            # Try to change the current character
            if changes_allowed > 0:
                for char in node.children:
                    if char != char_to_match:
                        if dfs(node.children[char], index + 1, changes_allowed - 1):
                            return True
            return False

        return dfs(self.root, 0, 1) # Start with 1 change allowed

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)