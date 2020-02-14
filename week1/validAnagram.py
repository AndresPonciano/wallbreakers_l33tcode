class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1 = (list(s))
        temp2 = (list(t))
        temp1.sort()
        temp2.sort()
        
        if temp1 == temp2:
            return True
        else: 
            return False