class Solution:
    def maxLength(self, arr: List[str]) -> int:
        memo = {}

        def has_duplicate(s, curr):
            dup = set(s)
            for ch in curr:
                if ch in dup:
                    return True

            return False

        def dfs(s, i):
            if i >= len(arr):
                return len(s)

            if (s, i) in memo:
                return memo[(s, i)]

            if len(set(arr[i])) != len(arr[i]) or has_duplicate(s, arr[i]):
                memo[(s, i)] = dfs(s, i + 1)
            else:
                memo[(s, i)] = max(dfs(s + arr[i], i + 1), dfs(s, i + 1))
                
            return memo[(s, i)]

        return dfs("", 0)

            