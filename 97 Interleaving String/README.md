# [97 Interleaving String](https://leetcode.com/problems/interleaving-string/description/)

This problem can either be solved through: 
1. Dynamic Programming 
2. Recursion + memoization 

I prefer recursion + memoization because it's more intuitive if you draw a decision tree. 

The recursive function will take in indices i, j, k of s1, s2, s3. They all start at 0. 

The memo dictionary will keep track of whether indices (i, j) can be interleaved to form s3[:k + 1]

### In each recursive call, you are checking one character only. This keeps it simple. 