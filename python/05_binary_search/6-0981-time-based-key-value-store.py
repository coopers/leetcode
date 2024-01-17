from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        TIMESTAMP, VALUE = 0, 1
        arr = self.store[key]
        if not arr or arr[0][TIMESTAMP] > timestamp:
            return ''

        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m][TIMESTAMP] <= timestamp:
                l = m + 1
            else:
                r = m

        return arr[r - 1][VALUE]