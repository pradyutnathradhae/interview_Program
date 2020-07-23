'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

'''

def myAtoi(self, st: str) -> int:
    n=0
    flag = flag2 = flag3 = 0
    sign_bit = 0
    limit = int(pow(2,31))
    dic = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,'5':5,'6':6,'7':7,
        '8':8,'9':9
    }
    for i in st:
        if i == ' ' and flag2 == 0:
            continue
        if i == '-' :
            if flag3 == 1:
                break
            flag=1
            flag2 = 1
            sign_bit += 1
        if i == '+':
            if flag3 == 1:
                break
            flag = 0
            flag2 = 1
            sign_bit += 1
        if not(i>='0' and i<='9') and i!= '-' and i!= '+' :
            break
        if i in dic:
            n = (n*10)+dic[i]
            flag2 = 1
            flag3 = 1
            
    if flag == 1:
        n = -n
    if sign_bit > 1:
        return 0
    if (flag==0 and n >= limit):
        return limit - 1
    elif (flag == 1 and abs(n) > limit):
        return -limit
    else:
        return n
    
