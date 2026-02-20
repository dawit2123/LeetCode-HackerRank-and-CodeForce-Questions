class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_info= [(p, s) for p, s in zip(position, speed)]
        car_info.sort(reverse=True)
        prev_time=(target-car_info[0][0])/car_info[0][1]
        result=1
        for i in range(1, len(car_info)):
            time= (target-car_info[i][0])/car_info[i][1]
            if time>prev_time:
                result+=1
                prev_time=time        
        return result
