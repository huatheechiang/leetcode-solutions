# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        #queue = 1, 5, 3, n, 4, 10, 6, 9, 2, n, n, n, n
        #bfs is usually not done recursively. you will probably use a queue...
        #turn the tree into a graph first (bidirectional graph)

        graph = defaultdict(list)
        
        def dfs(node, graph):
            if node is None:
                return

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)

            dfs(node.left, graph)
            dfs(node.right, graph)

        dfs(root, graph)

        count = -1
        visited = set()
        visited.add(start)

        queue = deque([start])
        new_queue = deque()

        while queue and len(visited) <= len(graph):
            
            print(queue)
            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        new_queue.append(neighbor)
                        visited.add(neighbor)
            
            count += 1
            queue = new_queue
            new_queue = deque()

        return count if count != -1 else 0

            