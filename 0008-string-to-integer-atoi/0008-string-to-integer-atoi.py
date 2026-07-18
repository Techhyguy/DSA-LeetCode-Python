class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Handle empty string after spaces
        if i == n:
            return 0

        # Handle sign
        sign = 1

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        result = 0

        while i < n and s[i].isdigit():

            digit = ord(s[i]) - ord('0')

            # Overflow check
            if result > INT_MAX // 10 or (
                result == INT_MAX // 10 and digit > 7
            ):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result