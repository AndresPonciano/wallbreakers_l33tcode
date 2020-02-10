class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # print(A)
        final = []
        odds = []
        for i in range(len(A)):
            if A[i]%2 == 0:
                final.append(A[i])
            else:
                odds.append(A[i])
                
        while(odds):
            final.append(odds.pop())
          
        return final
        # print(final)
        # print(odds)