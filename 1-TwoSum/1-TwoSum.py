class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in mapping:
                return [mapping[diff], i]

            mapping[nums[i]] = i
