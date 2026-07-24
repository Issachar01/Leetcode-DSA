class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        mine = 0
        for i in range(1, len(piles), 2):
            if i < len(piles):
                mine += piles[i]
            piles.pop()
        return mine