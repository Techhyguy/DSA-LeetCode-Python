from bisect import bisect_right
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        exact = [0] * (mx + 1)

        # Process from largest GCD to smallest
        for g in range(mx, 0, -1):

            cnt = 0

            # Count numbers divisible by g
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]

            pairs = cnt * (cnt - 1) // 2

            # Remove pairs with larger exact gcd
            for multiple in range(g * 2, mx + 1, g):
                pairs -= exact[multiple]

            exact[g] = pairs

        values = []
        prefix = []

        running = 0
        for g in range(1, mx + 1):
            if exact[g]:
                running += exact[g]
                values.append(g)
                prefix.append(running)

        ans = []

        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans