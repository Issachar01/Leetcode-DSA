class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num = []
        for i in range(m):
            num.append(nums1[i])
        for j in range(n):
            num.append(nums2[j])
        
        nums1[:] = sorted(num)
            
