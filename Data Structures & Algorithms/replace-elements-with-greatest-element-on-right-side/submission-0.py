class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            curr = arr[i]
            arr[i] = maxRight
            maxRight = max(curr, maxRight)
        arr[-1] = -1

        return arr


        
        