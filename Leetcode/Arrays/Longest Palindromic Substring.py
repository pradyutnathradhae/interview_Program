'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''

def lengtharoundcenter(s,l,r):
    while l >=0 and r< len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r-l-1

def longestPalindrome(s):
    if len(s) ==0 or s==None:
        return ""
    start = end = 0
    for i in range(len(s)):
        len1 = lengtharoundcenter(s,i,i)
        len2 = lengtharoundcenter(s,i,i+1)
        length = max(len1,len2)
        if length> (end-start):
            start = i - (length-1)//2
            end = i + length //2
    return s[start:end+1]

if __name__ == '__main__':
    print(longestPalindrome('xabbdy'))
    