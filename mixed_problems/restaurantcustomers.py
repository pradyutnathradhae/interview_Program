#First Approach
'''from collections import defaultdict

cnt = defaultdict(lambda : 0)
for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    for i in range(a,b+1):
        cnt[i] += 1

print(max(cnt.values()))'''

#Optimal Approach
arrival = []
leave = []
n = int(input())
for _ in range(n):
    a,b = list(map(int,input().split()))
    arrival.append(a)
    leave.append(b)

arrival.sort()
leave.sort()
i,j = 0,0
curr = 0
ma = 0
while i <n and j<n:
    if arrival[i]<leave[j]:
        curr += 1
        i += 1
    else:
        curr -= 1
        j += 1
    if curr > ma:
        ma = curr
print(ma)
    









