class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)

        for i in range(n):
            maxIndex = i
            for j in range(i+1, n):
                if heights[j] > heights[maxIndex]:
                    maxIndex = j
            heights[i], heights[maxIndex] = heights[maxIndex], heights[i]
            names[i], names[maxIndex] = names[maxIndex], names[i] 

        return names
            