class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        result = float('inf')
        curr_sum = 0
        q = deque()

        for r in range(len(nums)):
            curr_sum += nums[r]

            if curr_sum >= k:
                result = min(result, r + 1)
            
            while q and curr_sum - q[0][0] >= k:
                prefix, end_idx = q.popleft()
                result = min(result, r - end_idx)
            
            while q and q[-1][0] > curr_sum:
                q.pop()

            q.append((curr_sum, r))

        return -1 if result == float('inf') else result