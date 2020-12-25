'https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays'

def rotLeft(a, d):
    length = len(a)
    l = [None]*length
    for i in range(length):
        ind = i-d
        if ind < 0:
            ind += length
        l[ind] = a[i]
    return l