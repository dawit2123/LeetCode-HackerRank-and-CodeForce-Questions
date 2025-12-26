class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix_sum=[0]
        postfix_sum=[0]
        for i in range(len(customers)):
            if customers[i]=="N":
                prefix_sum.append(prefix_sum[-1]+1)
            else:
                prefix_sum.append(prefix_sum[-1])
        for j in range(len(customers)-1, -1,-1):
            if customers[j]=="Y":
                postfix_sum.append(postfix_sum[-1]+1)
            else:
                postfix_sum.append(postfix_sum[-1])
        postfix_sum=postfix_sum[::-1]
        result=[(prefix_sum[i]+postfix_sum[i]) for i in range(len(prefix_sum))]
        min_index=len(result)-1
        for i in range(len(result)-1, -1, -1):
            if result[i]<=result[min_index]:
                min_index=i
        return min_index