class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: (point[0], -point[1]))
        answer=0
        for i, (_, y1) in enumerate(points):
            max_y_value=float('-inf')
            for j in range(i+1, len(points)):
                if points[j][1]>max_y_value and points[j][1]<=y1:
                    max_y_value=points[j][1]
                    answer+=1                
        return answer