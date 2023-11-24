# 1561 Maximum Number of Coins You Can Get 
Given the following input array:

```
[2, 4, 1, 2, 7, 8]
```

The output should be 9

This question can easily be answered by sorting the input array

Sorted array:
```
[1, 2, 2, 4, 7, 8]
```
Answer will be the sum of the following:

```
[1, 2, **2**, 4, **7**, 8]
```

All you have to do is traverse the array from right to left, adding every _other_ element to a **res** variable len(array) // 3 times.

In this case, len(array) // 3 == 2.