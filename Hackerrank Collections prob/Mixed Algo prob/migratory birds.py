'https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen'

from collections import Counter
def migratoryBirds(arr):
    cnt = Counter(arr)
    maxval = max(cnt.values())
    minid = 6
    for i in cnt.keys():
        if maxval == cnt[i]:
            minid = min(minid,i)
    return minid