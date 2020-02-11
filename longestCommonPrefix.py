class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        print(prefix)
        for i in range(1, len(strs)):
            tempPrefix = ""
            for j in range(len(prefix)):
                if j > len(strs[i])-1 or strs[i][j] != prefix[j]:
                    break
                elif strs[i][j] == prefix[j]:
                    tempPrefix += prefix[j]
                    
            prefix = tempPrefix
        
        
        return prefix