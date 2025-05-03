# Problem: Tower of Hanoi  - https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

# User function Template for python3

class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        if n < 1:
            return 0
        
        return self.towerOfHanoi(n-1, fromm, aux, to)*2+1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):
        N = int(input())
        ob = Solution()
        print(ob.towerOfHanoi(N, 1, 3, 2))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends