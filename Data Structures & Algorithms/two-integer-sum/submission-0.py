class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        item_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in item_map:
                return [item_map.get(diff), i]
            item_map[nums[i]] = i