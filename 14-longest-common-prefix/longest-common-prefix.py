class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        sortedList= sorted(strs)
        sortedListFirst=sortedList[0]
        sortedListLast=sortedList[-1]
        for i in range(min(len(sortedListFirst), len(sortedListLast))):
            if(sortedListFirst[i]!= sortedListLast[i]):
                return ans
            else:
                ans+= sortedListFirst[i]
        return ans
        