class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        p1 = 0
        p2 = n - 1

        result = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[p1]) > abs(nums[p2]):
                num_sqr = nums[p1] ** 2
                p1 += 1 
            else:
                num_sqr = nums[p2] ** 2
                p2 -= 1
            result[i] = num_sqr
        
        return result 


                