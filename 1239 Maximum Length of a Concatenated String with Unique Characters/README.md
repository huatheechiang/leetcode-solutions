# [1239. Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/?envType=daily-question&envId=2024-01-23)

Since we have to consider every **subsequence**, we will perform backtracking with memoization.

For memoization, each key of the dictionary will be (s, i), where s is the current string and i is the current index. The value of each key will be the length of the longest string up to that point. 

If arr[i] has duplicate values in s, then skip arr[i] by calling memo[(s, i)] = dfs(s, i + 1)