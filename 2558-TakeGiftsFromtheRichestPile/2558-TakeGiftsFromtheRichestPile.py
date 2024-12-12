class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            n = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -floor(sqrt(n)))
        
        return -sum(max_heap)