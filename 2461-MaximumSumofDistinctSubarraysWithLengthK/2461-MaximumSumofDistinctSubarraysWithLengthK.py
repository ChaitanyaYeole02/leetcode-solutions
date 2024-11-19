class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prev_idx = {}
        l = 0
        result, curr_sum = 0, 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            i = prev_idx.get(nums[r], -1)

            while l <= i or r - l + 1 > k:
                curr_sum -= nums[l]
                l += 1

            if r - l + 1 == k:
                result = max(result, curr_sum)
            
            prev_idx[nums[r]] = r

        return result
        