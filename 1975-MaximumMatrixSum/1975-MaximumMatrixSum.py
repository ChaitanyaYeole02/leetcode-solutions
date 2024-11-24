class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = 0
        neg_cnt = 0
        mat_min = float('inf')

        for row in matrix:
            for n in row:
                result += abs(n)
                mat_min = min(mat_min, abs(n))

                if n < 0:
                    neg_cnt += 1
        
        if neg_cnt & 1:
            result -= (2 * mat_min)

        return result