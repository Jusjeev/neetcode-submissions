class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Don't use modulo that is affecting time complexity between my earlier time complexity and best complexity even if small
        # Don't overcomplicate even if it seems smarter in mind!
        n = len(nums)
        ans = [0] * (n * 2)
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
        