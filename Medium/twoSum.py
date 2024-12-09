class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     n = len(numbers)
    #     for i in range(n):
    #         for j in range(n):
    #             if numbers[i] + numbers[j] == target:
    #                 return [numbers[i],numbers[j]]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r = 0, n-1
        curSum = 0
        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum < target:
                l += 1
            if currSum > target:
                r -= 1
            if currSum == target:
                return [l+1,r+1]
            