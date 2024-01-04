class Solution:
    def minOperations(self, nums: List[int]) -> int:
        buff = {}

        for n in nums:
            if n in buff:
                buff[n] += 1
            else:
                buff[n] = 1

        res = 0
        for n in buff:
            if buff[n] == 1:
                return -1 

            res += buff[n] // 3

            if buff[n] % 3 != 0:
                res += 1 

        return res