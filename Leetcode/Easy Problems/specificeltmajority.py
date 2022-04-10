'''https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/'''
from collections import Counter
import math
class Solution(object):
    def isMajorityElement(self, nums,target):
        """
        :type nums: List[int]
        :rtype: int
        """
        return True if Counter(nums)[target] > math.floor(len(nums)/2) else False

print(Solution().isMajorityElement([2,4,5,5,5,5,5,6,6],5))
print(Solution().isMajorityElement([10,100,101,101],101))