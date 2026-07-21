class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")

        t = "1" + s + "1"

        runs = []
        i = 0

        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        gain = 0

        for i in range(1, len(runs) - 1):
            ch, _ = runs[i]

            if ch == "1":
                left_char, left_len = runs[i - 1]
                right_char, right_len = runs[i + 1]

                if left_char == "0" and right_char == "0":
                    gain = max(gain, left_len + right_len)

        return ones + gain