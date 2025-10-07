class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area=0
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    x1, y1= points[i][0], points[i][1]
                    x2, y2= points[j][0], points[j][1]
                    x3, y3= points[k][0], points[k][1]
                    area= abs(0.5*(x1*(y2-y3)+ x2*(y3-y1)+x3*(y1-y2)))
                    max_area= max(max_area, area)
        return max_area