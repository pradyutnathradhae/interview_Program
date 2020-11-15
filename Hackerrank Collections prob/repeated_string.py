'https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup'

def repeatedString(s, n):
    length = len(s)
    val = n // length
    temp = n % length
    count = 0
    subcount = 0
    for i in range(length):
        if s[i] == 'a':
            count += 1
        if i == temp - 1:
            subcount = count
    val *=count
    val +=subcount
    return val