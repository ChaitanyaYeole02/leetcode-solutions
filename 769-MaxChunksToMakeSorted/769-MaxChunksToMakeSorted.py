class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curr_max = -1
        result = 0

        for i, n in enumerate(arr):
            curr_max = max(n, curr_max)

            if curr_max == i:
                result += 1
        
        return result
