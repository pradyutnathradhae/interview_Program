'https://www.hackerrank.com/challenges/magic-square-forming/problem'

from itertools import *
def formingMagicSquare(s):
    X = []
    X.extend(s[0])
    X.extend(s[1])
    X.extend(s[2])
    Ans = 81
    for P in permutations(range(1,10)):
        if sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and P[0] + P[4] + P[8] == 15 and (P[2] + P[4] + P[6] == 15):
            Ans = min(Ans, sum(abs(P[i] - X[i]) for i in range(0,9)))
    return Ans
            