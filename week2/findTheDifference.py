class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = collections.Counter()
        for i in range(len(s)):
            letters[s[i]] += 1
                
        for j in range(len(t)):            
            if t[j] not in letters:
                letters[t[j]] += 1
            else:
                if letters[t[j]] == 1:
                    del letters[t[j]]
                else:
                    letters[t[j]] -= 1
                
        for k in letters:
            return k