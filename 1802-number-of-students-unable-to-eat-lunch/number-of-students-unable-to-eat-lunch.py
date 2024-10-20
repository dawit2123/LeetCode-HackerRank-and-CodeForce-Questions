class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res=len(students)
        count=Counter(students)
        for s in sandwiches:
            if count[s]>0:
                res-=1
                count[s]-=1
            else:
                return res
        return res