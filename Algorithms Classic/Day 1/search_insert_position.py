'''
https://leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

'''

#Better solution than previous solution in Easy section
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        k=-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                k = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if k != -1:
            return k
        else:
            k = min(l,r)
            if nums[k] < target:
                return k+1
            else:
                return max(0,k)