# [155 Min Stack](https://leetcode.com/problems/min-stack/description/)

The key to this problem is implementing a solution with O(1) time complexity for each function 

This is the challenging part: 
```
int getMin() retrieves the minimum element in the stack.
```

The solution: initialize a stack which keeps track of the current value **and** the min value at that point in a tuple 

The int getMin() function will return stack[-1][1]