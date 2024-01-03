class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        buff = []
        arr.sort()
        m = arr[int((len(arr) - 1) / 2)]

        for n in arr:
            buff.append((n, abs(n - m)))
            
        sorted_buff = sorted(buff, key = lambda x: (-x[1], -x[0]))

        res = []
        for i in range(k):
            res.append(sorted_buff[i][0])
                
        return res
