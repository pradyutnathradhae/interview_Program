'https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps'


from collections import Counter

# Complete the sherlockAndAnagrams function below.
def calc(n):
    return (n*(n-1))//2
def sherlockAndAnagrams(s):
    count = 0
    dic = Counter(s)
    for i in range(2,len(s)):
        for j in range(0,len(s)-i+1):
            sb = s[j:j+i]
            dic["".join(sorted(sb))] += 1
    for i in dic.values():
        count += calc(i)
    return count