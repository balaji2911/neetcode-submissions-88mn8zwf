class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        item_map = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in item_map:
                return [item_map.get(diff), i]
            item_map[n] = i