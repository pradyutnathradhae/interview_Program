'https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem'

def breakingRecords(scores):
    minval = scores[0]
    maxval = scores[0]
    a,b=0,0
    for i in scores:
        if minval > i:
            b += 1
            minval = i
        if maxval < i:
            a += 1
            maxval = i
    return a,b