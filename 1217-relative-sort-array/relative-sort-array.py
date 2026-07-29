class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Map the value of arr2 to to its index
        rank = {val: i for i, val in enumerate(arr2)}

        # Custom Comparator
        def customComparator(n):

            if n in arr2:
                return(0, rank[n])
            else:
                return(1, n)

        arr1.sort(key=customComparator)
        return arr1
