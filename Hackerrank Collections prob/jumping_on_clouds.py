'https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup'


def jumpingOnClouds(c):
    n = len(c)
    count = 0
    flag = 0
    ind = 0
    while ind < n-1:
        if n - ind -1 >= 2 and c[ind+2] == 0:
            ind += 2
            count += 1
        elif c[ind+1] == 0:
            ind += 1
            count += 1
        else:
            flag = 1
            break
    if flag == 1:
        return 0
    else:
        return count