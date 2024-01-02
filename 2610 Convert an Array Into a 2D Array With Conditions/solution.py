class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        buff = {}

        for n in nums:
            if n in buff:
                buff[n] += 1
            else:
                buff[n] = 1 

        sorted_buff = sorted(buff.items(), key = lambda x: -x[1])

        res = []

        for k, v in sorted_buff:
            if len(res) == 0:
                for i in range(v):
                    res.append([k])
            else:
                for i in range(v):
                    res[i].append(k)

        return res