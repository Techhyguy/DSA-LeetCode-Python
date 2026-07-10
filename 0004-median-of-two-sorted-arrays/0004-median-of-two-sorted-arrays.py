from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        left_size = (m + n + 1) // 2

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = left_size - cut1

            # Values around partition in nums1
            left1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            right1 = float("inf") if cut1 == m else nums1[cut1]

            # Values around partition in nums2
            left2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            right2 = float("inf") if cut2 == n else nums2[cut2]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd total number of elements
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                # Even total number of elements
                return (max(left1, left2) + min(right1, right2)) / 2

            # We took too many elements from nums1
            elif left1 > right2:
                high = cut1 - 1

            # We took too few elements from nums1
            else:
                low = cut1 + 1