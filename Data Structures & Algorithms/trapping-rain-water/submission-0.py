class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculates trapped rainwater using a Two-Pointer approach.
       
        ALGORITHM OVERVIEW:
        This approach optimizes the Dynamic Programming solution by replacing arrays
        with two pointers and two variables, reducing space complexity from O(n) to O(1).


        THE "BOTTLENECK" PRINCIPLE:
        Water trapped at any index 'i' is limited by the shorter of its two tallest
        boundaries (left_max and right_max).
        - If left_max < right_max, the 'left_max' is the definitive bottleneck for the
          left pointer. We don't need to know the exact height of the
          true right_max; we just need to know it is taller than the current left_max.
        - We calculate water at the current 'left' or 'right' pointer based on
          whichever side has the smaller boundary.


        INCLUSIVE BOUNDARIES:
        Like the DP approach, we initialize left_max and right_max with the heights
        at the pointers. This "inclusive" logic ensures that if
        a bar is the tallest boundary itself, the calculation (max_boundary - height[i])
        yields 0, gracefully preventing negative water values.


        COMPLEXITY:
        - Time: O(n) as we traverse the list once with two pointers meeting in the middle.
        - Space: O(1) as we only store a few integer variables.


        EXAMPLE:
        Input: [4, 2, 0, 3]
        1. left=0 (h=4), right=3 (h=3). left_max=4, right_max=3.
        2. right_max < left_max: Process right. water += (3 - 3) = 0. right moves to 2.
        3. left_max=4, right_max=max(3, 0)=3.
        4. right_max < left_max: Process right. water += (3 - 0) = 3. right moves to 1.
        ... and so on until pointers meet.
        """


        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0


        while left < right:
            if left_max < right_max:
                water_trapped += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])


            else:
                water_trapped += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])


        return water_trapped
