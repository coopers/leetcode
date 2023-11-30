from typing import List

    
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        remaining = {0, 1, 2}
        for t in triplets:
            if all(t[i] <= target[i] for i in range(3)):
                remaining -= {i for i in remaining if t[i] == target[i]}
                if not remaining:
                    return True

        return False

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = 0
        x, y, z = target
        for u, v, w in triplets:
            if u <= x and v <= y and w <= z:
                a, b, c = map(max, ((a, u), (b, v), (c, w)))
                if a == x and b == y and c == z:
                    return True
        return False
    

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = {i for t in triplets if all(t[i] <= target[i] for i in range(3)) for i in range(3) if t[i] == target[i]}
        return len(res) == 3
    
