
def climbStairs(n):
    l = [None]*(n+1)
    l[0] = 1
    l[1] = 1
    for i in range(2,n+1):
        l[i] = l[i-1] + l[i-2]
    return l[n]