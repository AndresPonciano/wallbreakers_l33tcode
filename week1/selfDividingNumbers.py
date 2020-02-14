class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        final = []
        for i in range(left, right+1):
            if i < 10:
                final.append(i)
            else:
                res = [int(x) for x in str(i)] 
                flag = 0
                for j in range(len(res)):
                    if res[j] == 0 or i%res[j] != 0:
                        flag = 1
                        break
                if flag == 0:
                    final.append(i)
                            
                            
                # print(res)

        return final