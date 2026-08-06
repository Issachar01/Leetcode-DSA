class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        target_sum = skill[0] + skill[n-1]

        left = 0 
        right = n - 1
        total_chemistry = 0 
        while left < right:
            if skill[left] + skill[right] != target_sum:
                return -1
            total_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        return total_chemistry
            
        