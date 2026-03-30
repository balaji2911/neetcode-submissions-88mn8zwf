class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        res = []
        right = len(nums) - 1

        for left in range(1,len(nums)):
            prefix.append(nums[left-1]*prefix[left - 1])
            suffix.append(nums[right]*suffix[left - 1])
            right -= 1

        suffix.reverse()
        print(suffix)
        print(prefix)
        for i in range(len(prefix)):
            res.append(prefix[i]*suffix[i])

        return res
        
        
            