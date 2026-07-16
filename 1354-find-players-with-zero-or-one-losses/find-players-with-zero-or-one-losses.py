class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        for winner, losser in matches:
            if winner not in losses:
                losses[winner] = 0
            losses[losser] = losses.get(losser, 0) + 1
        W = sorted([ k for k, v in losses.items() if v == 0])
        L = sorted([ k for k, v in losses.items() if v == 1])
        arr = [W, L]
        return arr
            
        
           