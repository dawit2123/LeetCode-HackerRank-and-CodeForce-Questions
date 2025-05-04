# Problem: Josephus Problem - https://www.geeksforgeeks.org/josephus-problem/


    # initialize two variables i and ans
    i = 1
    ans = 0
    while(i <= n):

        # update the value of ans
        ans = (ans + k) % i
        i += 1
    
    # returning the required answer
    return ans + 1