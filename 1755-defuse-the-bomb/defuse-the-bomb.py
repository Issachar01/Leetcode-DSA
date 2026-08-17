class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decode = [0] * n
        
        if k == 0:
            return decode
            
        for i in range(n):
            current_sum = 0
            if k > 0:
                for j in range(1, k + 1):
                    current_sum += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    current_sum += code[(i - j) % n]
            
            decode[i] = current_sum
            
        return decode