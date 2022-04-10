'''https://leetcode.com/problems/merge-sorted-array/'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ind1 = m
        ind2 = n
        ival = 0
        for i in range(m+n-1,-1,-1):
            if ind1 == 0 or ind2 == 0:
                ival = i
                break
            if nums1[ind1-1] >nums2[ind2-1]:
                nums1[i] = nums1[ind1-1]
                ind1 -= 1
            else:
                nums1[i] = nums2[ind2-1]
                ind2 -= 1
        if ind1 == 0 and ind2 == 0 :
            pass
        elif ind1 != 0:
            for i in range(i,-1,-1):
               nums1[i] = nums1[ind1-1] 
               ind1 -= 1
        else:
            for i in range(i,-1,-1):
               nums1[i] = nums2[ind2-1]
               ind2 -= 1
        return nums1

ob = Solution()
print(ob.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(ob.merge([1],1,[],0))
print(ob.merge([0],0,[1],1))