class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeats = {}
        for i in range(len(s)):
            if s[i] not in repeats.keys():
                repeats[s[i]] = [1, i]
            else:
                repeats[s[i]][0] +=1
                
        print(repeats)
        
        for j in repeats:
            if repeats[j][0] == 1:
                return repeats[j][1]
                
        return -1