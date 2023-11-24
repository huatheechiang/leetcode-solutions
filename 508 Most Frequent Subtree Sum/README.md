# [508 Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/description/)

Calculate the subtree sum of every node by using dfs recursion and store the answer in a dictionary

Dictionary's key is the subtree sum 
Dictionary's value is the number of times the subtree sum has appeared 

Once you have created your dictionary, manipulate it by sorting. Return the correct answer

The key for dfs recursion in this problem:
```
subtree_sum = node.val + dfs(node.left, buff) + dfs(node.right, buff)
```

The base case is:
```
if not node:
    return 0
```

And at the end we will return:

```
return subtree_sum
```