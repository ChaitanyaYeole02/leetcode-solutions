class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        result = [0] * len(queries)
        items.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])
        max_beauty = 0
        j = 0

        for q, i in queries:
            while j < len(items) and items[j][0] <= q:
                max_beauty = max(max_beauty, items[j][1])
                j += 1
            
            result[i] = max_beauty

        return result