class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        toGive = {5:0, 10:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                toGive[bills[i]] += 1
            elif bills[i] == 10:
                if toGive[5] > 0:
                    toGive[10] += 1
                    toGive[5] -= 1
                else:
                    return False
            else:
                if toGive[10] > 0 and toGive[5] > 0:
                    toGive[10] -= 1
                    toGive[5] -= 1
                elif toGive[10] == 0 and toGive[5] > 2:
                    toGive[5] -= 3
                else:
                    return False
                
        return True   