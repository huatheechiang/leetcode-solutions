class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * len(nums1) for i in range(len(nums2))]
        res = 0

        for j in range(len(dp)):
            for i in range(len(dp[0])):
                if nums1[i] == nums2[j]:
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[j][i] = 1 + dp[j - 1][i - 1]
                    else:
                        dp[j][i] = 1

                    res = max(res, dp[j][i])

        return res