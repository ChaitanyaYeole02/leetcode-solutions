class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Remove prefix
        N = len(arr)
        r = N - 1

        while r and arr[r - 1] <= arr[r]:
            r -= 1
        
        result = r

        # Remove postfix and middle
        l = 0

        while l < r:        
            # Expand Invalid window
            while r < N and arr[l] > arr[r]:
                r += 1
            
            result = min(result, r - l - 1)

            if arr[l] > arr[l + 1]:
                break
            
            l += 1
        
        return result
