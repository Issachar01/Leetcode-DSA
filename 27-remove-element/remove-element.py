class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer = 0
        for reader in nums:
                if reader != val:
                    nums[writer] = reader
                    writer += 1
        return writer
            