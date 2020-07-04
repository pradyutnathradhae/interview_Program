'''
MICROSOFT INTERVIEW 2020

Leetcode 1239. Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

'''

def maxLength(arr):
    temp = ['']
    res = 0
    for i in arr:
        for uniq in temp:
           if len(set(uniq+i)) == len(uniq) + len(i):
               temp.append(i+uniq)
               res= max(res,len(temp[-1]))
    return res    

if __name__ == '__main__':
    print(maxLength(["un", "iq", "ue"]))
    print(maxLength(["cha", "r", "act", "ers"]))
    print(maxLength(["yy", "bkhwmpbiisbldzknpm"]))

