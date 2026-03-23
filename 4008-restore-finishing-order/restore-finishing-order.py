class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_order=[]
        friends_set=set(friends)
        for id in order:
            if id in friends_set:
                friends_order.append(id)
        return friends_order