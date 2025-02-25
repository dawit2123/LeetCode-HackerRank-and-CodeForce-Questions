from collections import Counter  
from typing import List  

class Solution:  
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:  
        size = len(img1)  # Use img1 instead of A  
        overlap_count = Counter()  
        
        for i in range(size):  
            for j in range(size):  
                if img1[i][j] == 1:  # Use img1 instead of A  
                    for h in range(size):  
                        for k in range(size):  
                            if img2[h][k] == 1:  # Use img2 instead of B  
                                overlap_count[(i - h, j - k)] += 1  
        
        # No colon at the end  
        return max(overlap_count.values()) if overlap_count else 0