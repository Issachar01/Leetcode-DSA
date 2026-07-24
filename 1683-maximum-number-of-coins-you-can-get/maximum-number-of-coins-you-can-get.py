class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        mine = 0
        for i in range(1, 2 * len(piles) // 3, 2):
            mine += piles[i]
            
        return mine