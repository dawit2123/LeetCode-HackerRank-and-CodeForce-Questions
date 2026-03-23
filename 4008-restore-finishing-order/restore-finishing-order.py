class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_order=[]
        for id in order:
            if id in friends:
                friends_order.append(id)
        return friends_order