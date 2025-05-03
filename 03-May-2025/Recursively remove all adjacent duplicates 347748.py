# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

#User function Template for python3

class Solution:
    def removeUtil (self, S):
		sb = ""
        # Get the size of the input string
        n = len(S)
    
        # Iterate over the length of current string
        i = 0
        while i < n:
            # Flag to check if the current character
            # is repeated
            repeated = False
    
            # Check if the current characte
            # r is the same as the next one
            while i + 1 < n and S[i] == S[i + 1]:
                # Mark as repeated
                repeated = True
                # Skip the next character since
                # it's a duplicate
                i += 1
    
            # If the character was not repeated, 
            # add it to the result string
            if not repeated:
                sb += S[i]
            i += 1
    
        # If no changes were made, return the result
        # string
        if n == len(sb):
            return sb
        # Otherwise, recursively call the function \
        # to check for more duplicates
        return self.removeUtil(sb)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        s = ob.removeUtil(S)
        if len(s) == 0:
            print("\"\"")
        else:
            print(s)

        print("~")

# } Driver Code Ends