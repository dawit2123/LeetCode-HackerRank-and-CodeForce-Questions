class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_num1=m-1
        last_num2=n-1
        position=len(nums1)-1
        while last_num2>=0 and last_num1>=0:
            if nums2[last_num2] > nums1[last_num1]:
                nums1[position]=nums2[last_num2]
                last_num2-=1
            else:
                nums1[position]=nums1[last_num1]
                last_num1-=1
            position-=1
        while last_num2>=0:
            nums1[position]=nums2[last_num2]
            position-=1
            last_num2-=1