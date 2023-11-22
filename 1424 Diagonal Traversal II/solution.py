class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        buff = {}
        for j in range(len(nums)):
            for i in range(len(nums[j])):
                diagonal_value = i + j
                if diagonal_value not in buff:
                    buff[diagonal_value] = [nums[j][i]]
                else:
                    buff[diagonal_value].append(nums[j][i])
        
        res = []
        for key in buff:
            buff[key].reverse()
            res.extend(buff[key])

        return res