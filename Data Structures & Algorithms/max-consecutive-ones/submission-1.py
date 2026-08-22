class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = 0
        curLength = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curLength +=1
            elif nums[i] == 0:
                curLength = 0
            maxLength = max(maxLength, curLength)
        return maxLength
        