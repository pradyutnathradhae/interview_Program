'''https://leetcode.com/problems/squares-of-a-sorted-array'''
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([i*i for i in nums])