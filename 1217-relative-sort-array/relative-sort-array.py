class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Step 1: Map each element in arr2 to its index (priority)
        # Example: arr2 = [2, 1, 4, 3, 9, 6] becomes {2: 0, 1: 1, 4: 2, 3: 3, 9: 4, 6: 5}
        rank = {val: idx for idx, val in enumerate(arr2)}
        
        # Step 2: Define a custom sorting key function
        def custom_key(x):
            # If the number exists in arr2, return its rank (comes first)
            # If the number is NOT in arr2, push it to the end by returning a high number (inf) 
            # and sort those remaining numbers normally by using x as a secondary sort value.
            if x in rank:
                return (0, rank[x])
            else:
                return (1, x)
        
        # Step 3: Sort arr1 using our custom key function
        arr1.sort(key=custom_key)
        
        return arr1