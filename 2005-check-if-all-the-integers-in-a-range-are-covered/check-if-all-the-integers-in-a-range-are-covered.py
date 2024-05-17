class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges.sort()
        for start, end in ranges:
            if end<left: continue
            if start>left: return False
            if end>=right: return True 
            left= end +1
        
        
         