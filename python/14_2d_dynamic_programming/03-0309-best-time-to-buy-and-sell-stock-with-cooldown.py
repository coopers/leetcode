from typing import List
import math


class Solution(object):
    def maxProfit(self, prices):
        profit, cost, carry = 0, math.inf, 0
        for price in prices:
            profit, cost, carry = price - cost, min(cost, price - carry), max(profit, carry)

        return max(profit, carry)


class Solution(object):
    def maxProfit(self, prices):
        L = len(prices)
        MP = [0] * (L + 2)

        for i in reversed(range(L)):
            # Case 1). buy and sell the stock
            C1 = 0
            for sell in range(i + 1, L):
                profit = (prices[sell] - prices[i]) + MP[sell + 2]
                C1 = max(profit, C1)

            # Case 2). do no transaction with the stock p[i]
            C2 = MP[i + 1]

            # Choose best case
            MP[i] = max(C1, C2)

        return MP[0]
    