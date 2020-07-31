'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
'''
def count(a,b,c):
    count = 0
    if a == '1':
        count += 1
    if b== '1':
        count += 1
    if c == '1':
        count += 1
    return count
def sumchar(a,b,c):
    count1 = count(a,b,c)
    if count1 == 0:
        return ('0','0')
    elif count1 == 1:
        return ('0','1')
    elif count1 == '2':
        return ('1','0')
    else:
        return ('1','1')

def addBinary(a, b):
    resstr = ""
    carry = "0"
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    temp_a = len(a)-1
    temp_b = len(b)-1
    while temp_a >= 0 and temp_b >= 0:
        carry,res = sumchar(a[temp_a],b[temp_b],carry)
        resstr = res + resstr
        temp_a -= 1
        temp_b -= 1
    if temp_a >= 0:
        while temp_a >= 0:
            carry,res = sumchar(a[temp_a],'0',carry)
            resstr = res + resstr
            temp_a -= 1
    if temp_b >= 0:
        while temp_b >= 0:
            carry,res = sumchar('0',b[temp_b],carry)
            resstr = res + resstr
            temp_b -= 1
    if carry == '1':
        resstr = '1' + resstr 
    return resstr
    
#Working Solution

def addBinary2(self, a: str, b: str) -> str:
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    sum = bin(int(a,2) + int(b,2))
    return str(sum[2:])