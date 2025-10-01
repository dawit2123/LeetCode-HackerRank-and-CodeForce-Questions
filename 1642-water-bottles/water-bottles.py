class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        num_of_bottles_you_can_drink=numBottles
        while numBottles>=numExchange:
            num_of_bottles_you_can_drink+=(numBottles//numExchange)
            numBottles=(numBottles//numExchange)+(numBottles%numExchange)
        return num_of_bottles_you_can_drink