from typing import List

# N: length of digits
# Time:  O(N ✖️ 4^N)
# Space: O(N), depth of the recursion call stack
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

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

        def backtrack(chosen, i):
            if i == len(digits):
                res.append(''.join(chosen))
            else:
                for c in digitToChar[digits[i]]:
                    chosen.append(c)
                    backtrack(chosen, i + 1)
                    chosen.pop()

        res = []
        backtrack([], 0)

        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def helper(chosen, remaining):
            if not remaining:
                res.append(''.join(chosen))
            else:
                for ch in m[remaining[0]]:
                    helper(chosen + [ch], remaining[1:])

        digits = [*digits]
        helper([], digits)
        return res