# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        number_of_arrows=1
        if len(points)<1:
            return 0
        for i in range(1, len(points)):
            if points[i][0]>=points[i-1][0] and points[i][0]<=points[i-1][1]:
                points[i][1]=min(points[i][1],points[i-1][1])
            else:
                number_of_arrows+=1
        return number_of_arrows