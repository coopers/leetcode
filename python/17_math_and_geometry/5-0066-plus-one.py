from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) -1, -1, -1):
            digits[i] = 0 if digits[i] == 9 else digits[i] + 1
            if digits[i] != 0:
                return digits

        return [1] + digits
