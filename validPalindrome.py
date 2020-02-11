class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 or not s:
            return True
        
        mid = int(len(s)/2)
        end = len(s)-1
        
        left = []
        right = []
        flag = 0
        for i in range(mid+1):
            print(s[i], s[end])
            if s[i].isalnum():
                left.append(s[i].lower())
                flag = 1
            
            if s[end].isalnum():
                right.append(s[end].lower())
                flag = 1
            end -= 1
            
        # if flag == 0:
            # return True
        print(left)
        print(right)
        
        if len(left) == 1 and not right:
            return True
        elif len(right) == 1 and not left:
            return True
            
        while True:
            if len(right) > len(left):
                temp = right.pop()
                print(temp)
            elif len(left) > len(right):
                temp = left.pop()
                print(temp)
            
            if len(left) == len(right):
                break
            
            left.append(temp)
            print(len(left), len(right))


        print(str(left))
        print(str(right))
        
        if not left or not right:
            return False
                
        if str(left) == str(right):
            print("pee")
            return True
        else:
            return False