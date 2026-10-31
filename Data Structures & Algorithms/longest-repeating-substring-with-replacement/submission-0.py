class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        longest = 0
        maxfreq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxfreq = max(maxfreq, count[s[right]])

            if (right - left + 1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest