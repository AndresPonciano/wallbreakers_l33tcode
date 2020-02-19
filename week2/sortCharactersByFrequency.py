class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter()
        
        for i in range(len(s)):
            counter[s[i]] += 1
                    
        final = ""
        for j in counter.most_common():
            final += j[0]*j[1]
            
        return(final)