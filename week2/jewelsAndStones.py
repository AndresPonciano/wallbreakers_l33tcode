class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {}
        for i in range(len(J)):
            jewels[J[i]] = i
            
        
        count = 0
        
        for j in range(len(S)):
            if S[j] in jewels.keys():
                count += 1
                
        return count
                