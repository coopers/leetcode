class Solution(object):
    def isHappy(self, n):
        s = {n}
        while n != 1:
            n = sum([int(d) * int(d) for d in str(n)])
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
        return 1 if n == 1 else sum([int(d) * int(d) for d in str(n)])
    
class Solution(object):
    def isHappy(self, n: int) -> bool:
        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        while n != 1 and n not in cycle_members:
            n = get_next(n)

        return n == 1