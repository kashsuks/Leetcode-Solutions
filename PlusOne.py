from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numArr = []
        strDigits = ''
        for i in digits:
            strDigits += str(i)
        num = int(strDigits) + 1
        strDigits = str(num)

        for i in strDigits:
            numArr.append(int(i))

        return numArr