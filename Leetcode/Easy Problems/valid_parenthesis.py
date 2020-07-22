'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

def isValid(s):
    l = []
    dic = {
        '(':')',
        '{':'}',
        '[':']',
        ']':'1',
        ')':'2',
        '}':'3'
    }
    for i in s:
        if len(l) == 0 or dic[l[-1]] != i:
            l.append(i)
        else:
            l.pop()
    if len(l) == 0:
        return True
    else:
        return False