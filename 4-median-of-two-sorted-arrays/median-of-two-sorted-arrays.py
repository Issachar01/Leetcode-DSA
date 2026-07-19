class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        data = sorted(nums1 + nums2)
        if len(data)%2 == 0:
            pose = len(data)//2 - 1
            median = float((data[pose] + data[pose + 1])/2)
        else:
            pose = int((len(data) + 1)/2 - 1)
            median = data[pose]
        return median