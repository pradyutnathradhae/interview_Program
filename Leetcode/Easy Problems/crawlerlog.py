'''https://leetcode.com/problems/crawler-log-folder/'''
class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        l=[]
        for log in logs:
            if log == './':
                pass
            elif log == '../':
                if len(l) != 0:
                    l.pop()
            else:
                l.append(log)
        return len(l)