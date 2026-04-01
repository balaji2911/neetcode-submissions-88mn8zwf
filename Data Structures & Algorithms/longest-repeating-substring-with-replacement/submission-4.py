from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l,r = 0,0
        res = 0

        while r < len(s):
            counts[s[r]] += 1
            if r - l + 1 - counts[max(counts, key = counts.get)] <= k:
                r += 1
                res = max(res, r-l+1)
            else:
                counts[s[l]] -= 1
                l += 1
                r += 1 

        return res - 1
                
