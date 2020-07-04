'''
Leetcode:137
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

'''


def singleNumber(nums):
    dic = {}
    for i in nums:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    for i in dic.keys():
        if dic[i] < 3:
            return i

def if_numbers_less_than_3(nums):
    s = sum(nums)
    return s % 3

def another_approach(nums):
    r = (3*(sum(set(nums))) - sum(nums))//2
    return r

if __name__=='__main__':
    print(singleNumber([0, 1, 0, 1, 0, 1, 99]))
    print(singleNumber([2, 2, 3, 2]))
    print(if_numbers_less_than_3([2,2,1,2]))
