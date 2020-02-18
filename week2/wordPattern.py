class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        list1 = str.split()
        
        if len(list1) != len(pattern):
            return False
        
        results = {}
        for i in range(len(pattern)):
            if pattern[i] not in results.keys() and list1[i] not in results.values():
                results[pattern[i]] = list1[i]
            else:
                if pattern[i] in results.keys():
                    if results[pattern[i]] != list1[i]:
                        return False
                elif list1[i] in results.values():
                    if pattern[i] not in results.keys():
                        return False
                
        return True