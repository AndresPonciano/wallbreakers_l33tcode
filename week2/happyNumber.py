class Solution:
    def isHappy(self, n: int) -> bool:
        
        print(n)
        flag = 0
        result = 0
        results = {}
        thing = str(n)
        while flag != 1:
            for i in range(len(thing)):
                result += (int(thing[i])**2)
                
            thing = str(result)
            flag = result
            
            if flag in results.keys():
                break
            
            results[flag] = flag
            result = 0
            
        if 1 in results.keys():
            return True