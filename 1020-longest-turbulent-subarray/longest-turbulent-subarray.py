class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l=0
        r=1
        max_length=1
        previous=""
        while(r<len(arr)):
            if arr[r-1]< arr[r] and previous!="<":
                max_length=max(max_length, r-l+1)
                r+=1
                previous="<"
            elif arr[r-1]> arr[r] and previous!=">":
                max_length= max(max_length, r-l+1)
                r+=1
                previous=">"
            else:
                previous=""
                l= r if arr[r-1]==arr[r] else r-1
                r= r+1 if arr[r-1]== arr[r] else r
        return max_length
