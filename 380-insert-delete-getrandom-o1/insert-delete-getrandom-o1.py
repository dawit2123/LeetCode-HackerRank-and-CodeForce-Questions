class RandomizedSet:

    def __init__(self):
        self.num_map={}
        self.num_list=[]

    def insert(self, val: int) -> bool:
        res=val not in self.num_map
        if res:
            self.num_map[val]=len(self.num_list)
            self.num_list.append(val)
        return res

    def remove(self, val: int) -> bool:
        res=val in self.num_map
        if res:
            # get the index of the val
            index_val= self.num_map[val]
            # replace the value of the val with the end of the list
            last_value=self.num_list[-1]
            self.num_list[index_val]=last_value
            # pop the las value as it's not needed
            self.num_list.pop()
            # update the num_map with the index of val
            self.num_map[last_value]=index_val
            # remove the val from the num_map
            del self.num_map[val]
        return res
    def getRandom(self) -> int:
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()