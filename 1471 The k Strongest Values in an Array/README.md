# [1471. The k Strongest Values in an Array](https://leetcode.com/problems/the-k-strongest-values-in-an-array/description/)

Hardest part is understanding what the question is asking. 

Question is asking you to sort the array in a specific way and to return the k largest elements. 

To solve the problem, sort the array first prioritizing abs(arr[i] - m) and then arr[i].

Lastly, return the k largest elements. 