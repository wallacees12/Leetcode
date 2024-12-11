class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Brute Force
        # n = len(temperatures)
        # res = []

        # for i in range(n):
        #     k = i
        #     if i == n-1:
        #         res.append(0)

        #     while temperatures[k] <= temperatures[i]:
        #         if k == n-1:
        #             res.append(0)
        #             break
        #         k += 1
        #     res.append(k - i)
            
        # return res
    
        n = len(temperatures)
        stack = [] # pair [temp, index]
        res = [0] * n

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackidx = stack.pop()
                res[stackidx] = (i - stackidx)
                
            stack.append([t, i]) 

        return res


