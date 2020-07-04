'''
Leetcode:205

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character but a character may map to itself.

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
'''


def isIsomorphic(s, t):
    dic = {}
    flag = True
    for i in range(len(s)):
        if s[i] in dic.keys():
            if t[i] != dic[s[i]]:
                flag = False
                break
        else:
            if t[i] in dic.values():
                flag = False
                break
            dic[s[i]] = t[i]
    return flag


if __name__ == '__main__':
    print(isIsomorphic('foo', 'bar'))
    print(isIsomorphic('paper','title'))
