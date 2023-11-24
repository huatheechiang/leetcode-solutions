class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        times = len(piles) // 3
        res = 0
        count = 0 

        for i in range(1, len(piles), 2):
            if count == times:
                break

            count += 1
            res += piles[i]

        return res
        