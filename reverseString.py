class Solution:
    def reverseString(self, s: List[str]) -> None:
        mid = int(len(s)/2)
        reverse = len(s)-1
        for i in range(mid):
            temp = s[i]
            s[i] = s[reverse]
            s[reverse] = temp
            reverse -= 1