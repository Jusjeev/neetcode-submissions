class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        end_index = len(nums) - 1
        while i <= end_index:
            if nums[i] == val:
                # remove code
                for idx in range(i, len(nums) - 1):
                    nums[idx] = nums[idx + 1]
                end_index -= 1
            elif nums[i] != val:
                k += 1
                i += 1
        return k

        
        