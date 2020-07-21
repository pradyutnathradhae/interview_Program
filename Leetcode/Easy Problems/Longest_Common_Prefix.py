'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''
def checkequality(arr,index):
    ch = arr[0][index]
    for i in arr:
        if i[index] != ch:
            return 1
    return 0

def longestCommonPrefix(strs):
    flag = 0
    prefix = ""
    if len(strs) == 0:
        return ""
    min_length = len(strs[0])
    for i in strs:
        if len(i)<min_length:
            min_length = len(i)
    i = 0
    while flag == 0 and i<min_length:
        flag = checkequality(strs,i)
        if flag == 0:
            prefix = prefix + strs[0][i]
        i +=1
    return prefix