'''https://leetcode.com/problems/top-k-frequent-elements/'''

from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = Counter(nums)
        keys = cnt.keys()
        keys = sorted(keys,key=lambda x: cnt[x],reverse=True)[:k]
        return keys
