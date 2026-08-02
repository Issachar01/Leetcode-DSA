class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        set2 = set(nums2)
        for num in nums1:
            if num in set2:
                return num
        return -1