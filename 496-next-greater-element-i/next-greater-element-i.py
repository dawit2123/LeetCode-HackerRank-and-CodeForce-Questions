class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer=[-1]*len(nums1)
        num_to_index= {n:i for i, n in enumerate(nums1)}
        stack=[]
        for num in nums2:
            while stack and num > stack[-1]:
                val=stack.pop()
                index=num_to_index[val]
                answer[index]=num
            if num in num_to_index:
                stack.append(num)
        return answer

            