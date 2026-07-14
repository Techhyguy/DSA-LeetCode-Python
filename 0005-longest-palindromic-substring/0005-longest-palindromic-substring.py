class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_length = 1

        for i in range(len(s)):

            # Odd length palindrome
            left = i
            right = i

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                current_length = right - left + 1

                if current_length > max_length:
                    start = left
                    max_length = current_length

                left -= 1
                right += 1

            # Even length palindrome
            left = i
            right = i + 1

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                current_length = right - left + 1

                if current_length > max_length:
                    start = left
                    max_length = current_length

                left -= 1
                right += 1

        return s[start:start + max_length]