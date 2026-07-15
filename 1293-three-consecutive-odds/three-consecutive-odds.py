class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag = False
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1:
                nextI = i + 1
                if arr[nextI] % 2 == 1:
                    finalI = i + 2
                    if arr[finalI] % 2 == 1:
                        flag = True
        return flag