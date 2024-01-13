class Solution:
    def minSteps(self, s: str, t: str) -> int:
        buff_s = {}
        for ch in s:
            if ch not in buff_s:
                buff_s[ch] = 1
            else:
                buff_s[ch] += 1

        buff_t = {}
        for ch in t:
            if ch not in buff_t:
                buff_t[ch] = 1
            else:
                buff_t[ch] += 1

        res = 0
        for ch in buff_s:
            if ch in buff_t and buff_s[ch] > buff_t[ch]:
                res += buff_s[ch] - buff_t[ch]
            elif ch not in buff_t:
                res += buff_s[ch]

        return res
