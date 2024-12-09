class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Sort and then iterate once use l and right points"""
        
        out = []
        nums.sort()


        for i, a in enumerate(nums):

            if i > 0 and a == nums[i-1]:
                continue

            #Here l = i + 1 start from the next element!
            l, r = i+1, len(nums) - 1
            while l < r:

                threesum = a + nums[l] + nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                elif threesum == 0:
                    out.append([a,nums[l],nums[r]])

                    # [-2, -2, 0, 0, 2, 2]
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return out