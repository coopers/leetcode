class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                i = i1 + i2
                res[i] += int(num1[i1]) * int(num2[i2])
                res[i + 1] += res[i] // 10
                res[i] = res[i] % 10

        while not res[-1]:
            res.pop()

        return "".join(map(str, res[::-1]))
