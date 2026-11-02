class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        countT = Counter(t)
        window = Counter()
        res = [-1, -1]
        reslen = float("inf")

        have, left = 0, 0
        need = len(countT)

        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1

            while have == need:
                if(right - left + 1) < reslen:
                    res = [left, right]
                    reslen = right - left + 1

                window[s[left]] -= 1

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r + 1] if reslen != float("inf") else ""