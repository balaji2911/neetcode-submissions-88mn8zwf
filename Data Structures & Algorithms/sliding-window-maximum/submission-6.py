class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)

            #print(r, r+k)
            if r - q[0] + 1 > k:
                #print(q[0])
                #print("Y")
                q.popleft()

            #print("Queue:", q)
            if r >= k-1:
                res.append(nums[q[0]])

        return res
        

