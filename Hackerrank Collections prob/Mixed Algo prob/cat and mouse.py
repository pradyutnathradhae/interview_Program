'https://www.hackerrank.com/challenges/cats-and-a-mouse/problem'

def catAndMouse(x, y, z):
    d1 = abs(z-x)
    d2 = abs(z-y)
    if d1 == d2:
        return 'Mouse C'
    elif d1 > d2:
        return 'Cat B'
    else:
        return 'Cat A'