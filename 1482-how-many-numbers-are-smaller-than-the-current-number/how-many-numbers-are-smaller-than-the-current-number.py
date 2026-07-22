class Solution:

  def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    first_index = {}
    for index, num in enumerate(sorted(nums)):
      if num not in first_index:
        first_index[num] = index

    return [first_index[num] for num in nums]
            


