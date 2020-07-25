'''
Non-decreasing Array
Easy

1876

456

Add to List

Share
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
 

Constraints:

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
'''
def checkPossibility(nums):
    counter = 0
    if len(nums) == 0:
        return False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            if i < 1 or nums[i-1] <= nums[i+1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i] 
            counter += 1
    if counter <= 1:
        return True
    else:
        return False