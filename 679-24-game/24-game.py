class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        num_list= [float(num) for num in cards]
        return self.dfs(num_list)
    # dfs function
    def dfs(self, num_list):
        if not num_list:
            return False
        if len(num_list)==1:
            return abs(num_list[0]-24.0)<1e-6
        for i in range(len(num_list)):
            for j in range(i+1,len(num_list)):
                for operation in range(6):
                    next_list_items= self.next_list_generator(num_list, i, j, operation)
                    if next_list_items and self.dfs(next_list_items):
                        return True
        return False
    
    # next_list function
    def next_list_generator(self, num_list, i, j, operation):
        next_list= [num_list[k] for k in range(len(num_list)) if k!= i and k !=j]
        if operation==0:
            # add value of i to value of j
            next_list.append(num_list[i]+num_list[j])
        elif operation==1:
            # subtract value of j from value of i
            next_list.append(num_list[i]-num_list[j])
        elif operation==2:
            # subtract value of i from value of j
            next_list.append(num_list[j]-num_list[i])
        elif operation==3:
            # multiply value of i by value of j
            next_list.append(num_list[i]*num_list[j])
        elif operation==4:
            if num_list[j]!=0:
                # divide value of i by value of j
                next_list.append(num_list[i]/num_list[j])
            else:
                return []
        elif operation==5:
            if num_list[i]!=0:
                # divide value of j by value of i
                next_list.append(num_list[j]/num_list[i])
            else:
                return []
        return next_list