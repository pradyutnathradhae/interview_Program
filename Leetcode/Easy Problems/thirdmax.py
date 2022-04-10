'''https://leetcode.com/problems/third-maximum-number/'''

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums),reverse=True)
        return nums[2] if len(nums)>= 3 else nums[0]