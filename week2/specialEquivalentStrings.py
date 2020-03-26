class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:

        evens = []
        odds = []
        groups = set()
        for i in range(len(A)):
            for j in range(len(A[i])):
                if j%2 == 0:
                    evens.append(A[i][j])
                else:
                    odds.append(A[i][j])
                    
            evens.sort()
            odds.sort()
            word = ''.join(evens+odds)
            groups.add(word)
            evens.clear()
            odds.clear()
            
        return len(groups)