class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        result = [0] * N

        if k == 0:
            return result

        l = 0
        curr_sum = 0

        for r in range(N + abs(k)):
            curr_sum += code[r % N]

            if r - l + 1 > abs(k):
                curr_sum -= code[l % N]
                l = (l + 1) % N
            
            if r - l + 1 == abs(k):
                if k > 0:
                    result[(l - 1) % N] = curr_sum
                else:
                    result[(r + 1) % N] = curr_sum

        return result