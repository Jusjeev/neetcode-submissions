class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        ans = [0] * (nums_size * 2)
        for i in range(len(ans)):
            ans[i] = nums[i%nums_size]
        return ans
        