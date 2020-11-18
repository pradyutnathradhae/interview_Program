'https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen'
'Solution:'
'https://www.youtube.com/watch?v=KZ8k9-22JmQ'



from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    after = Counter(arr)
    before = {}
    for i in arr:
        after[i] -= 1
        if after[i] == 0:
            after.pop(i)
        if i %r == 0:
            if i//r in before and i*r in after:
                count += (before[i//r] * after[i*r])
        if i in before:
            before[i] += 1
        else:
            before[i] = 1
    return count