# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    import bisect
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(houses)
        m = len(heaters)
        heaters.sort()
        ans = 0
        for house in houses:
            index = bisect.bisect_left(heaters, house)

            if index==0:
                nearest_heater_distance = heaters[0] - house
            elif index==m:
                nearest_heater_distance = house - heaters[-1]
            else:
                nearest_heater_distance = min(heaters[index]-house, house - heaters[index-1])
            ans = max(ans, nearest_heater_distance)
        return ans