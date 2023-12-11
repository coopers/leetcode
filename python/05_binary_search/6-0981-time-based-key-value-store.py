from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.h = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        TIMESTAMP, VALUE = 0, 1
        values = self.h[key]
        if not values or values[0][TIMESTAMP] > timestamp:
            return ''

        l, r = 0, len(values)
        while l < r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                l = m + 1
            else:
                r = m

        return values[r - 1][VALUE]