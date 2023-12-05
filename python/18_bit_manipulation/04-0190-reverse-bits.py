NUM_BITS = 32
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(NUM_BITS):
            res <<= 1
            if n & 1:
                res += 1
            n >>= 1

        return res