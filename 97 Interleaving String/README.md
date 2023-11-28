# [97 Interleaving String](https://leetcode.com/problems/interleaving-string/description/)

This problem can either be solved through: 
1. Dynamic Programming 
2. Recursion + memoization 

I prefer recursion + memoization because it's more intuitive if you draw a decision tree. 

The recursive function will take in indices i, j, k of s1, s2, s3. They all start at 0. 

The memo dictionary will keep track of whether indices (i, j) can be interleaved to form s3[:k + 1]

**In each recursive call, you are checking one character only. This keeps it simple.**

### Steps for recursion
1. Base case: if k == length(s3), then return True (it is possible to create the interleaved string)
2. Memoization step: if (i, j) is in memo, return memo[(i, j)]
3. Initialize an ans variable and set it equal to False
4. If i < length(s1) and s1[i] == s3[k], then recursively call the function, incrementing the index of i and k
5. If j < length(s2) and s2[j] == s3[k], then recursively call the function, incrementing the index of j and k
6. For both the if statements, set ans = ans or the result of the recursive call.  
7. Set memo[(i, j)] = ans
8. Return memo[(i, j)]


