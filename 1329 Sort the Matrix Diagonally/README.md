# [1329 Sort the Matrix Diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally/description/)

Each cell's coordinates is represented by (j, i). If diagonal_value = i - j, then all diagonal cells will have the same diagonal_value. 

The values in each diagonal in the matrix can be stored in a hashmap array. 

Sort the values in the array in ascending order. Then, iterate over the matrix and replace each (j, i) value with the sorted value in the buff, popping the value after placing it in the matrix.
