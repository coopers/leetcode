from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'qprs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(i, chosen):
            if i == len(digits):
                res.append(''.join(chosen))
            else:
                for c in digitToChar[digits[i]]:
                    chosen.append(c)
                    backtrack(i + 1, chosen)
                    chosen.pop()

        if digits:
            backtrack(0, [])

        return res
