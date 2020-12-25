'https://www.hackerrank.com/challenges/picking-numbers/problem'

from collections import Counter
def pickingNumbers(a):
    # Write your code here
    cnt = Counter(a)
    maxi = 0
    for i in a:
        c = cnt[i]
        d = cnt[i-1]
        c = c + d
        if c > maxi:
            maxi = c
    return maxi