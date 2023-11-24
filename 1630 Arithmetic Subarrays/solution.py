class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check_arithmetic(start, end):
            newArr = nums[start:end + 1]
            newArr.sort()

            diff = newArr[1] - newArr[0]

            for i in range(1, len(newArr)):
                if newArr[i] - newArr[i - 1] != diff:
                    return False

            return True

        res = []
        for i in range(len(l)):
            if check_arithmetic(l[i], r[i]):
                res.append(True)
            else:
                res.append(False)

        return res