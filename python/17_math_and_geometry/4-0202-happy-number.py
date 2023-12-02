class Solution(object):
    def isHappy(self, n):
        s = {n}
        while n != 1:
            n = sum(int(d) * int(d) for d in str(n))
            if n in s:
                return False
            s.add(n)
        return True
    

class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)
        while slow != fast:
            fast = self.sumSquareDigits(self.sumSquareDigits(fast))
            slow = self.sumSquareDigits(slow)

        return fast == 1

    def sumSquareDigits(self, n):
        return sum(int(d) * int(d) for d in str(n))
    
class Solution(object):
    def isHappy(self, n: int) -> bool:
        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}
        while n != 1 and n not in cycle_members:
            n = sum(int(d) * int(d) for d in str(n))

        return n == 1