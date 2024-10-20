from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue= deque(students)
        L=0
        while True:
            is_finished=True
            for i in range(len(queue)):
                if queue[i]== sandwiches[L]:
                    is_finished=False
            if is_finished:
                return len(queue)
            student=queue.popleft()
            if student==sandwiches[L]:
                L+=1
            else:
                queue.append(student)
        return -1