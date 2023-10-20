from typing import List



# Time   O(N)
# Space  O(N)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

        stack = []
        for t in tokens:
            if t in operations:
                b, a = stack.pop(), stack.pop()
                t = operations[t](a, b)
            stack.append(int(t))
            
        return stack.pop()

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b
