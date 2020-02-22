class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "":
            return True
        
        prev = 0
        for i in range(len(s)):
            for j in range(prev, len(t)):
                if s[i] == t[j]:
                    prev = j+1
                    if i == len(s)-1:
                        return True
                    break;
                else:
                    if j == len(t)-1:
                        return False
                    
        return False