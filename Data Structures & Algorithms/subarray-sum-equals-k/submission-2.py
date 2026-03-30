class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1 # For the edge case where first element itself is k
        currSum = 0
        ans = 0

        for num in nums:
            currSum += num
            ans += counts[currSum - k]
            counts[currSum] += 1
        
        return ans