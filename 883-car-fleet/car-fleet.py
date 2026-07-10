class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_stat=[(p,s) for p,s in zip(position, speed)]
        car_stat.sort()
        prev_time=(target-car_stat[-1][0])/car_stat[-1][1]
        result=1
        for i in range(len(car_stat)-2, -1, -1):
            time=(target-car_stat[i][0])/car_stat[i][1]
            if time>prev_time:
                prev_time=time
                result+=1
        return result
