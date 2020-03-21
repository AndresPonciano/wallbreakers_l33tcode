class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        newRow = len(A[0])
        newCol = len(A)
                
        array = [[0] * newCol for i in range(newRow)]

        for i in range(len(A)):
            for j in range(len(A[i])):
                array[j][i] = A[i][j]                
 
        return array