'https://www.hackerrank.com/challenges/drawing-book/problem'


def pageCount(n, p):
    #
    # Write your code here.
    #
    if p == 1 or p == n:
        return 0
    else:
        fromfront = p//2
        if n % 2 == 0:
            fromback = (n-p-1)//2 + 1
        else:
            fromback = (n - p)//2
        return min(fromfront,fromback)