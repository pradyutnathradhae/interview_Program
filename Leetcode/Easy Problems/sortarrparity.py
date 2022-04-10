
'''https://leetcode.com/problems/sort-array-by-parity/'''
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for i in nums:
            even.append(i) if i %2 ==0 else odd.append(i)
        return even + odd 