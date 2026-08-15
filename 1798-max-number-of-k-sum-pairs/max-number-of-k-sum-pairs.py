class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        operations = 0
        p1 = 0
        p2 = len(nums) - 1
        
        while p1 < p2:
            current_sum = nums[p1] + nums[p2]
            if current_sum < k:
                p1 += 1
            elif current_sum > k:
                p2 -= 1            
            else:
                operations += 1
                p1 += 1
                p2 -= 1

        return operations