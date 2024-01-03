class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        #time: O(m * n)
        #space: O(n)? Can be reduced to O(1)

        arr_laser = []

        for j in range(len(bank)):
            num_laser = 0
            for i in range(len(bank[0])):
                if bank[j][i] == '1':
                    num_laser += 1

            if num_laser > 0:
                arr_laser.append(num_laser)

        res = 0 
        for i in range(1, len(arr_laser)):
            res += arr_laser[i] * arr_laser[i - 1]

        return res