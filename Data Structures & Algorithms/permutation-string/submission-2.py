from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = Counter(s1)
        count_s2 = defaultdict(int)
        
        # 1. Build the very first window of size len(s1)
        for i in range(len(s1)):
            count_s2[s2[i]] += 1
        
        # 2. Check the first window immediately
        if count_s2 == count_s1:
            return True

        # 3. Slide the window across the rest of s2
        l = 0
        for r in range(len(s1), len(s2)):
            # Add the new character on the right
            count_s2[s2[r]] += 1
            # Remove the character on the left
            count_s2[s2[l]] -= 1
            
            # CRITICAL: Clean up keys with 0 count so comparison works
            if count_s2[s2[l]] == 0:
                del count_s2[s2[l]]
            
            l += 1
            
            # Check if the current window matches s1
            if count_s2 == count_s1:
                return True

        return False