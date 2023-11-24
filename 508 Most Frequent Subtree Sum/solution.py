# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        buff = {}

        def dfs(node, buff):
            if not node:
                return 0

            subtree_sum = node.val + dfs(node.left, buff) + dfs(node.right, buff)

            if subtree_sum not in buff:
                buff[subtree_sum] = 1
            else:
                buff[subtree_sum] += 1 

            return subtree_sum

        dfs(root, buff)
        buff_sorted = sorted(buff.items(), key = lambda x: x[1], reverse=True)

        res = []
        k = buff_sorted[0][1]
        for i, j in buff_sorted:
            if j == k:
                res.append(i)

        return res