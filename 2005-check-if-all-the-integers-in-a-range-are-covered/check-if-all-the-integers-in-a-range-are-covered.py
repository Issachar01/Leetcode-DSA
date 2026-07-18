class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        for target in range(left, right + 1):
            
            is_target_covered = any(start <= target <= end for start, end in ranges)
            
            if not is_target_covered:
                return False
                
        return True