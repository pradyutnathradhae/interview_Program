'''https://leetcode.com/problems/majority-element/'''

from collections import Counter
import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [i[0] for i in Counter(nums).items() if i[1] > math.floor(len(nums)/2) ][0]