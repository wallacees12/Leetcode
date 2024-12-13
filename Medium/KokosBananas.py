from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            c = 0
            for pile in piles:
                c += ceil(float(pile) / k)

            if c <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res   

