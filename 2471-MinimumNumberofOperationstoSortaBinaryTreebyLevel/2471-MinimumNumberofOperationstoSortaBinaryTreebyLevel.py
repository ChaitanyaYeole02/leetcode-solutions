# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def count_swap(nums):
            swaps = 0
            sorted_nums = sorted(nums)
            idx_map = {n: i for i, n in enumerate(nums)}

            for i in range(len(nums)):
                if nums[i] != sorted_nums[i]:
                    swaps += 1

                    j = idx_map[sorted_nums[i]]
                    nums[i], nums[j] = nums[j], nums[i]

                    idx_map[nums[j]] = j

            return swaps

        q = deque([root])
        result = 0

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            result += count_swap(level)
        
        return result
