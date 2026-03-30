class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            length = 1
            while num + 1 in nums_set:
                length += 1
                num += 1
            ans = max(ans,length)
        return ans

