'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

def maxSubArray(nums):
    if nums == []:
        return 0
    max_sum = sum(nums)
    sumval = 0
    for i in nums:
        sumval += i
        if sumval < i:
            sumval = i
        max_sum = max(sumval,max_sum)
    return max_sum