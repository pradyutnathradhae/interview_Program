'''https://leetcode.com/contest/weekly-contest-288/problems/largest-number-after-digit-swaps-by-parity/'''

class Solution:
    def largestInteger(self, num: int) -> int:
        evenind = []
        even = []
        oddind = []
        odd = []
        temp = str(num)
        length = len(temp)
        digits = [int(i) for i in temp]
        for i in range(length):
            if digits[i] %2 == 0:
                evenind.append(i)
                even.append(digits[i])
            else:
                oddind.append(i)
                odd.append(digits[i])
        even = sorted(even,reverse = True)
        odd = sorted(odd,reverse = True)
        for i in range(len(evenind)):
            digits[evenind[i]] = even[i]
        for i in range(len(oddind)):
            digits[oddind[i]] = odd[i]
        return int("".join([str(i) for i in digits]))

ob = Solution()
print(ob.largestInteger(1234))