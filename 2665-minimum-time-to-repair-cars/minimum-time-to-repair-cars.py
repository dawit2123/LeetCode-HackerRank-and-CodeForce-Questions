class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        result=-1
        def count_repaired(time):
            car_count=0
            for rank in ranks:
                car_count+=int(sqrt(time/rank))
            return car_count

        left, right= 1, ranks[0]*cars*cars
        while left<=right:
            mid=(left+right)//2
            repaired= count_repaired(mid)
            if repaired>=cars:
                result=mid
                right=mid-1
            else:
                left=mid+1
        return result