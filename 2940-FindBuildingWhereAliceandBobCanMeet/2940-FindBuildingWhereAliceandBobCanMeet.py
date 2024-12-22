class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1] * len(queries)

        groups = defaultdict(list) # r -> [(req_h, query_idx)]

        for i, q in enumerate(queries):
            l, r = sorted(q)

            if l == r or heights[r] > heights[l]:
                result[i] = r
            else:
                h = max(heights[l], heights[r])
                groups[r].append((h, i))
            
        min_heap = []

        for i, h in enumerate(heights):
            for q_h, q_i in groups[i]:
                heapq.heappush(min_heap, (q_h, q_i))
            
            while min_heap and h > min_heap[0][0]:
                q_h, q_i = heapq.heappop(min_heap)
                result[q_i] = i

        return result
        