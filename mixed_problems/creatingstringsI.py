from itertools import permutations

s = input().rstrip()
permut = permutations(s)
l = set()
for i in list(permut):
    l.add(''.join(i))

l = sorted(list(l))
print(len(l))
for i in l:
    print(i)