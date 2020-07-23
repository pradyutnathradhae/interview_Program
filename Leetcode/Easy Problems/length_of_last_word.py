'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''

def lengthOfLastWord(s):
    if len(s) == 0:
        return 0
    st_list = s.split(' ')
    #if len(st_list) == 0:
    #    return len(s)
    length = len(st_list[0])
    for i in range(len(st_list)-1,0,-1):
        if len(st_list[i]) >= 1:
            length = len(st_list[i])
            break
    return length