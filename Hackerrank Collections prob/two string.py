'https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps'

from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d = Counter(s1)
    flag = 0
    for i in s2:
        if i in d:
            flag = 1
            break
    if flag == 1:
        return 'YES'
    else:
        return 'NO'