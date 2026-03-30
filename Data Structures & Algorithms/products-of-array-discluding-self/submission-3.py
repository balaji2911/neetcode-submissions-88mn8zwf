class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        left = 1
        right = len(nums) - 2

        for i in range(1, len(nums)):
            res.append(nums[right+1] * res[i-1])
            right -= 1

        res.reverse()
        
        for j in range(len(nums)):
            res[j] *= left
            left *= nums[j]

        return res

        
        
        
            