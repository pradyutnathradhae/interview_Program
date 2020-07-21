'''
15. 3Sum
Medium

7265

831

Add to List

Share
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
def threeSum(nums):
    nums.sort()
    l = len(nums)
    retList = []
    for i in range(l):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        start = i + 1
        end = l - 1
        while(start < end):
            if nums[i] + nums[start] + nums[end] == 0:
                retList.append([nums[i] , nums[start] , nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start-1]:
                    start += 1
                while start < end and nums[end] == nums[end+1]:
                    end -= 1
            elif nums[i] + nums[start] + nums[end] > 0:
                end -= 1
                # while start < end and nums[end] == nums[end+1]:
                #     end -= 1
            elif nums[i] + nums[start] + nums[end] < 0:
                start += 1
                # while start < end and nums[start] == nums[start-1]:
                #     start += 1                    
    return retList

if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))