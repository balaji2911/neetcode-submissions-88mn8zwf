from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for key,vals in counts.items():
            heapq.heappush(heap, (vals,key))

            if len(heap) > k:
                heapq.heappop(heap)

        return [nums[1] for nums in heap]