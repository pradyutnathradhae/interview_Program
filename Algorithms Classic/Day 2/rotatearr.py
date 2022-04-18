'''https://leetcode.com/problems/rotate-array/'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        k = k % len(nums)
        l = 0
        r = k-1
        temp = None
        while l<=r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1
        l = k
        r = len(nums)-1
        while l<=r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1