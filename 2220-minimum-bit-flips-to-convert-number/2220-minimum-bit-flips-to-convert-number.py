class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        count = 0

        while xor:
            xor &= (xor - 1)
            count += 1

        return count