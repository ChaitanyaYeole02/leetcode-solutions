class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        result = 0

        def dfs(curr, parent):
            total = values[curr]

            for child in adj[curr]:
                if child != parent:
                    total += dfs(child, curr)
            
            if total % k == 0:
                nonlocal result

                result += 1
            
            return total

        dfs(0, -1)

        return result