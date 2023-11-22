#H1 1424 Diagonal Traversal

Consider the following matrix:
1 2 3 
4 5 6 
7 8 9 

It will have the following indices:
[0][0] [0][1] [0][2]
[1][0] [1][1] [1][2]
[2][0] [2][1] [2][2]

What happens if we sum the indices?
For example, if we sum the indices [0][2] we will get 0 + 2 = 2 
0 1 2
1 2 3
2 3 4 

Notice that all the indices sums with the same value are diagonals. 
Therefore, we can traverse the array, saving the values with similar indices sums in a dictionary.

The dictionary can then be manipulated to return the correct answer. 