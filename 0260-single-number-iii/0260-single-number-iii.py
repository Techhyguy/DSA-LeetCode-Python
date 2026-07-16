class Solution:
    def singleNumber(self, nums):
        xor = 0

        for num in nums:
            xor ^= num

        rightmost_bit = xor & (-xor)

        first = 0
        second = 0

        for num in nums:
            if num & rightmost_bit:
                first ^= num
            else:
                second ^= num

        return [first, second]