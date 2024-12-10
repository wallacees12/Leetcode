class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            v = [int(i) for i in list(str(n))]
            n = 0
            for k in v:
                n += k**2
        
        return True
