'''https://leetcode.com/problems/binary-search/'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind = -1
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                ind = mid
                break
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        return ind
            