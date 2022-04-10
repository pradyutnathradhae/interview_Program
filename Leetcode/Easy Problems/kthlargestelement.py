'''https://leetcode.com/problems/kth-largest-element-in-an-array/'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums,reverse= True)[k-1]