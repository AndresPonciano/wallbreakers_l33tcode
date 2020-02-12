class Solution:
    def findComplement(self, num: int) -> int:
        # print(format(5, "b"))
        
        temp = format(num, "b")
        temp2 = ""
        for i in range(len(temp)):
            if temp[i] == '1':
                temp2 += '0'
            else:
                temp2 += '1'

        return int(temp2, 2)