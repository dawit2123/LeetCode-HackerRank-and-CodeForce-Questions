class Trie:

    def __init__(self):
        self.trieNode = {"end": False}
    def insert(self, bit):
        pnt = self
        for i in bit:
            if i not in pnt.trieNode:
                pnt.trieNode[i] = Trie()
            pnt = pnt.trieNode[i]
        pnt.trieNode["end"] = True

    def search(self, bit):
        pnt = self
        ans = ''
        for i in bit:
            if i == '0':
                if "1" in pnt.trieNode:
                    pnt = pnt.trieNode['1']
                    ans += '1'
                    continue
                pnt = pnt.trieNode['0']
                ans += '0'
            else:
                if "0" in pnt.trieNode:
                    pnt = pnt.trieNode['0']
                    ans += '1'
                    continue
                pnt = pnt.trieNode['1']
                ans += '0'
        return int(ans,2)
                    



class Solution:
    def sort_2d_with_index(self,arr):
        indexed_arr = [(i, row) for i, row in enumerate(arr)]
        indexed_arr.sort(key=lambda x: x[1][1])  # Sorting by second element of each row
        sorted_arr = [row[1] for row in indexed_arr]  # Sorted rows
        original_indices = [row[0] for row in indexed_arr]  # Original indices
        return sorted_arr, original_indices

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trieObj = Trie()
        result = [-1 for i in range(len(queries))]
        newQ, indArr = self.sort_2d_with_index(queries)
        nums.sort()
        start = 0
        for row, i in enumerate(newQ):
            xV,cV = i
            if(cV<nums[0]):
                continue
            
            for j in range(start,len(nums)):
                if(nums[start] > cV):
                    break
                binary = format(nums[start],'032b')
                trieObj.insert(binary)
                start += 1
            binary = format(xV,'032b')
            result[indArr[row]] = trieObj.search(binary)
        return result