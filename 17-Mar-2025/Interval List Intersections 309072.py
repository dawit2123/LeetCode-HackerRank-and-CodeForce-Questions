# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections_result=[]
        first_list_index= second_list_index= 0
        while first_list_index<len(firstList) and second_list_index<len(secondList):
            start_intersection= max(firstList[first_list_index][0], secondList[second_list_index][0])
            end_intersection= min(firstList[first_list_index][1], secondList[second_list_index][1])
            if start_intersection<=end_intersection:
                intersections_result.append([start_intersection, end_intersection])
            if firstList[first_list_index][1]<secondList[second_list_index][1]:
                first_list_index+=1
            else:
                second_list_index+=1
        return intersections_result