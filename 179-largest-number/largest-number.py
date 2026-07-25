class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        str_nums = list(map(str, nums))
        str_nums.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else (-1 if x + y > y + x else 0)))
        result = "".join(str_nums)
        return "0" if result[0] == "0" else result