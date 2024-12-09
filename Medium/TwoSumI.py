class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Hash map to store the idx of a number with the difference we need to hit target
        indicies = {}

        for i, n in enumerate(nums):
            #Set the numbers up with their index in nums
            indicies[n] = i
        
        for i,n in enumerate(nums):
            #How far away from target are we?
            diff = target - n
            #Do we have a number that fits that description and isnt the current number i.e. no repeats?
            if diff in indicies and indicies[diff] != i:
                return [i,indicies[diff]]
                
