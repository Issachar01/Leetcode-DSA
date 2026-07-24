class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                indices.append(i)
        return indices
