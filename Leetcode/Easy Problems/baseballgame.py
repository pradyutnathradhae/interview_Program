'''https://leetcode.com/problems/baseball-game/'''
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        vals = []
        for op in ops:
            if op == "C":
                vals.pop()
            elif op == "D":
                vals.append(vals[-1]*2)
            elif op == "+":
                vals.append(vals[-1]+vals[-2])
            else:
                vals.append(int(op))
        return sum(vals)
        