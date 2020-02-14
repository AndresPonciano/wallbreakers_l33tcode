class Solution:
    def binaryGap(self, N: int) -> int:
        temp = bin(N)
        flag = 0
        dist = 0
        tempDist = 0
        print(temp)
        for i in range(len(temp)):
            if temp[i] == '1' and flag == 0:
                flag = 1
            elif temp[i] == '1' and flag == 1:
                tempDist += 1
                if tempDist > dist:
                    dist = tempDist
            
                tempDist = 0
                
            if flag == 1 and temp[i] == '0':
                tempDist += 1
                
                
        return dist