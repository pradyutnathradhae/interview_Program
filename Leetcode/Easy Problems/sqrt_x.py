'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''

def mySqrt(self, x: int) -> int:
    if x == 0 or x == 1:
        return x
    flag = 0
    i = 1
    res = 0
    while flag == 0:
        power = pow(i,2)
        if power == x:
            res = i
            flag = 1
        if power > x:
            res = i - 1
            flag = 1
        i += 1
    return res

