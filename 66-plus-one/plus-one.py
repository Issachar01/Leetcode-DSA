class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0 
        for i in digits:
            num = num*10 + i
        num = str(num+1)
        digits = []
        for i in range(len(num)):
            digits.append(int(num[i]))
        return digits


        
        