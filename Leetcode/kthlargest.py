'''https://leetcode.com/problems/kth-largest-element-in-a-stream/'''

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums,reverse=True)[:self.k]
        if self.k == len(self.nums):
            self.prev = self.nums[-1]
        else:
            self.prev = 0
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.k > len(self.nums):
            self.nums.append(val)
            self.nums = sorted(self.nums,reverse=True)[:self.k]
            self.prev = self.nums[-1]
            return self.prev            
        elif val <= self.prev:
            return self.prev
        else:
            for i in range(self.k):
                if self.nums[i] < val:
                    self.nums.insert(i,val)
                    self.nums.pop()
                    break
            self.prev = self.nums[-1]
            return self.prev

ob = KthLargest(1,[])
print(ob.add(-3))
print(ob.add(-2))