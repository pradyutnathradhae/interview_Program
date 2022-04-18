'''https://leetcode.com/problems/reverse-string-ii/'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        strlist = [i for i in s]
        for i in range(0,len(strlist),2*k):
            strlist[i:i+k] = reversed(strlist[i:i+k])
        return "".join(strlist)