class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # print(digits)
        final = []
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[len(digits)-1] < 9:
                digits[i] += 1
                return digits
            elif digits[i] == 9 and carry == 0:
                carry = 0
                final.insert(0, 0)
                if i == 0:
                    final.insert(0, 1)

            else:
                if carry == 0:
                    final.insert(0, digits[i]+1)
                    carry = 1
                elif carry == 1:
                    final.insert(0, digits[i])

        return(final)