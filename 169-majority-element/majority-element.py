class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencyDict = Counter(nums)
        # Returns a list of all matching keys
        keys = [k for k, v in frequencyDict.items() if v > len(nums)/2][0]  
        return keys      