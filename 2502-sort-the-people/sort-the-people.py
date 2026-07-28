class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)

        for i in range(1, n):
            key_height = heights[i]
            key_name = names[i]
            j = i - 1
            while j >= 0 and key_height > heights[j]:  
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            heights[j + 1] = key_height
            names[j + 1] = key_name

        return names