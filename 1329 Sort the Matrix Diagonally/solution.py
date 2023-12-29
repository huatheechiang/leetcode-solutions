class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        buff = {}

        for j in range(len(mat)):
            for i in range(len(mat[0])):
                if i == 0 or j == 0 and (j - i) not in buff:
                    buff[i - j] = [mat[j][i]]
                else:
                    buff[i - j].append(mat[j][i])

        for k in buff:
            buff[k] = sorted(buff[k], reverse=True)

        for j in range(len(mat)):
            for i in range(len(mat[0])):
                mat[j][i] = buff[i - j].pop()

        return mat