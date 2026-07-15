class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        Harshad = -1
        digit_sum = 0
        temp = x
        while temp > 0:
            digit_sum += temp%10
            temp //= 10
        if x % digit_sum == 0:
            Harshad = digit_sum
            return Harshad 
        return Harshad
