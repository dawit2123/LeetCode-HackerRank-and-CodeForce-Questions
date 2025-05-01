# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

#User function Template for python3

class Solution:
    def printTillN(self, N):
    	def recursion(value):
    	    if value==0:
    	        return
    	    recursion(value-1)
    	    print(value, end=" ")
    	recursion(N)
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTillN(N)
        print()
# } Driver Code Ends