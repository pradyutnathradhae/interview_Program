'''https://leetcode.com/contest/weekly-contest-287/problems/minimum-number-of-operations-to-convert-time/'''

class Solution:
    def convertTime(self, current, correct):
        curr = [int(i) for i in current.split(":")]
        corr = [int(i) for i in correct.split(":")]
        difftime = (corr[0]*60 + corr[1]) - (curr[0]*60 + curr[1])
        count = 0
        while difftime > 0:
            if difftime>=60:
                count += 1
                difftime -= 60
            elif difftime >= 15 and difftime <60:
                count += 1
                difftime -= 15
            elif difftime >= 5 and difftime <15:
                count += 1
                difftime -= 5
            else:
                count += 1
                difftime -= 1
        return count  
        



        