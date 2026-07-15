class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for x in range(32):
            if n == 2**x:
                return True
                break
        return False