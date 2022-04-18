'''https://leetcode.com/contest/weekly-contest-289/problems/calculate-digit-sum-of-a-string/'''
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        st = s
        while len(st) > k:
            temp = ""
            for i in range(0,len(st),k):
                temp += str(sum([int(i) for i in st[i:i+k]]))
            st = temp
            # print(temp)
        return st

print(Solution().digitSum("11111222223", 3))