class Solution:

  def pancakeSort(self, arr: List[int]) -> List[int]:
    res = []
    n = len(arr)

    # Work backwards from the largest possible value down to 1
    for x in range(n, 0, -1):
      # Find the index of the current target value 'x'
      idx = arr.index(x)

      # If it's already at its correct position (the end of the current unsorted section), skip
      if idx == x - 1:
        continue

      # If the element is not already at the beginning (index 0), flip it to the front
      if idx != 0:
        res.append(idx + 1)
        arr[: idx + 1] = arr[: idx + 1][::-1]

      # Flip the element from the front to its correct target position at the end of the unsorted segment
      res.append(x)
      arr[:x] = arr[:x][::-1]

    return res