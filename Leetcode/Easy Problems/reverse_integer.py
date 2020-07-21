'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.

'''

def reverse(x):
    limit = int(pow(2,31))
    rev = rem = 0
    flag = 0
    if x < 0:
        flag = 1
    x = abs(x)
    while x != 0:
        rem = x % 10
        rev = (rev * 10) + rem
        x = x // 10
    if flag == 1:
        rev = -rev
    if (flag==0 and rev >= limit) or (flag == 1 and abs(rev) > limit):
        return 0
    else:
        return rev