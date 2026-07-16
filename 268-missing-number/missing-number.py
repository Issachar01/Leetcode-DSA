class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = -1
        for num in nums:
            i += 1
            if i != num:
                return i
                exit()
        return i+1
             