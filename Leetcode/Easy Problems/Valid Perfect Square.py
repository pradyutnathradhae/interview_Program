'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
'''
def isPerfectSquare(self, x: int) -> bool:
    if x == 1:
        return True
    flag = 0
    i = 1
    while flag == 0:
        power = pow(i,2)
        if power == x:
            flag = 1
        if power > x:
            break
        i += 1
    if flag == 1:
        return True
    else:
        return False