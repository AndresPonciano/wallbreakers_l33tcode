class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        count = 0
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    s[j] = -1
                    count += 1
                    break
                    
        return count