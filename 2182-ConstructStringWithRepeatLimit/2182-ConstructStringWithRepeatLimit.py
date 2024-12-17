class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)

        max_heap = [(-ord(c), cnt) for c, cnt in count.items()]
        heapq.heapify(max_heap)

        result = []

        while max_heap:
            char, cnt = heapq.heappop(max_heap)
            char = chr(-char)
            curr_cnt = min(cnt, repeatLimit)
            result.append(char * curr_cnt)

            if cnt - curr_cnt > 0 and max_heap:
                nxt_char, nxt_cnt = heapq.heappop(max_heap)
                nxt_char = chr(-nxt_char)
                result.append(nxt_char)
                
                if nxt_cnt > 1:
                    heapq.heappush(max_heap, (-ord(nxt_char), nxt_cnt - 1))
                
                heapq.heappush(max_heap, (-ord(char), cnt - curr_cnt))
        
        return "".join(result)
