class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        longest = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1

            while (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1

            longest = max(longest, R - L + 1)

        return longest
        