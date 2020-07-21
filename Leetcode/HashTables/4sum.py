'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

def twosum(nums,target):
    res = []
    dic = {}
    for i in range(len(nums)):
        if (target - nums[i]) in dic:
            res.append(dic[target-nums[i]])
            res.append(i)
            break
        else:
            dic[nums[i]] = i
    return res

if __name__ == '__main__':
    print(twosum([2,7,11,15],9))