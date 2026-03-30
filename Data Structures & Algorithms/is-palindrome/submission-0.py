class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join([char for char in s if char.isalnum()]).lower()
        l, r = 0, len(s1) - 1

        while l <= r:
            if s1[l] != s1[r]:
                return False
            l += 1
            r -= 1
        return True
