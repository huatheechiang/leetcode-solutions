class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''
        1 2 3 
        4 5 6
        7 8 9

        [0][0] [0][1] [0][2]
        [1][0] [1][1] [1][2] 
        [2][0] [2][1] [2][2]
        [3][0] [3][1] [3][2] 
        '''
        
        buff = {}
        for j in range(len(nums)):
            for i in range(len(nums[j])):
                diagonal_value = i + j
                if diagonal_value not in buff:
                    buff[diagonal_value] = [nums[j][i]]
                else:
                    buff[diagonal_value].append(nums[j][i])
        # print(buff)
        res = []
        for key in buff:
            buff[key].reverse()
            res.extend(buff[key])

        return res