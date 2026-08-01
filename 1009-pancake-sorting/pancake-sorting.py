class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k = []
        n = len(arr)

        for x in range(n,0,-1):
            idx = arr.index(x)

            if idx == x - 1:
                continue

            if idx != 0:
                k.append(idx + 1)
                arr[:idx+1] = arr[:idx+1][::-1]
            
            k.append(x)
            arr[:x] = arr[:x][::-1]

        return k     