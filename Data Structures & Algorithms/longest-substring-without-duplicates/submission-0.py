class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        left = 0
        right = 0
        ans = 0
        seen = defaultdict(int)

        while right < len(s):
            if seen[s[right]] < 1:
                seen[s[right]] += 1
                ans = max(ans, right - left + 1)
                right += 1

            else:
                seen[s[left]] -= 1
                left += 1
                
           

        return ans
