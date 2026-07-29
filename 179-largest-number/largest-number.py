class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        strs = [str(n) for n in nums]
        
        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0
                
        # Sort using the custom key
        strs.sort(key=cmp_to_key(compare))
        
        # Join the sorted strings
        result = "".join(strs)
        
        # Handle edge case where the result starts with '0' (e.g., [0, 0])
        return "0" if result[0] == "0" else result