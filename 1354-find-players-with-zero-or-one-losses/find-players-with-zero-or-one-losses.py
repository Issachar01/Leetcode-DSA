class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        arrW = {player[0] for player in matches}

        losser = {}
        for players in matches:
            losser[players[1]] = losser.get(players[1], 0) + 1
        
        arrL1 = sorted([playerL for playerL in losser if losser[playerL] == 1])
        arrWAll = sorted(list(W for W in arrW if W not in losser))

        return [arrWAll, arrL1]


        
                       
            
        
        
            
                


        
        
           