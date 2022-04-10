'''https://leetcode.com/problems/backspace-string-compare/'''

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        res_s = []
        res_t = []
        for i in s:
            if i == "#":
                if len(res_s) != 0:
                    res_s.pop()
            else:
                res_s.append(i)
        for i in t:
            if i == "#":
                if len(res_t) != 0:
                    res_t.pop()
            else:
                res_t.append(i)
        if res_s == res_t:
            return True
        else:
            return False