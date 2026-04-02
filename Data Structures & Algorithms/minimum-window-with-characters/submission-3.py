class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        count_t = Counter(t)
        count_s = defaultdict(int)
        need, have = len(t), 0
        l, r = 0, 0
        ans_l, ans_r = -1, -1
        ans_len = float('inf')
        
        while r < len(s):
            if s[r] in count_t.keys():
                count_s[s[r]] += 1
                if count_s[s[r]] <= count_t[s[r]]:
                    have += 1
            while have == need:
                if r-l+1 < ans_len:
                    ans_l, ans_r = l, r
                    ans_len = ans_r - ans_l + 1
                if s[l] in count_t:
                    count_s[s[l]] -= 1
                    if count_s[s[l]] < count_t[s[l]]:
                        have -= 1
                l += 1
            r += 1

        return s[ans_l:ans_r+1] if ans_r - ans_l + 1 != float("inf") else ""
