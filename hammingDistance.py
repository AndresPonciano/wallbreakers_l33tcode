class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        count = 0
        a = format(a, "b")
        for i in range(len(a)):
            if a[i] == '1':
                count += 1
                
        return count