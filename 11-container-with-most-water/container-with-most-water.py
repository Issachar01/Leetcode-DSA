class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPt = 0
        rightPt = len(height) - 1

        max_water = 0

        while leftPt < rightPt:
            current_height = min(height[leftPt], height[rightPt])
            current_width = rightPt - leftPt
            water = current_height * current_width 
            if water > max_water:
                max_water = water
            if height[leftPt] < height[rightPt]:
                leftPt += 1
            else:
                rightPt -= 1

        return max_water
