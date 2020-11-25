def fibonacciModified(t1, t2, n):
    t3 = 0
    for _ in range(n-2):
        t3 = t1 + (t2**2)
        t1 = t2
        t2 = t3
    return t3