# [1630 Arithmetic Subarrays](https://leetcode.com/problems/arithmetic-subarrays/description)

How will you check if a sequence of numbers in a list is arithmetic?

1. Sort the list of numbers
2. Determine diff, where diff = nums[1] - nums[0]
3. Iterate through the list of numbers, if nums[i] - nums[i - 1] != diff, then the list isn't arithmetic 

