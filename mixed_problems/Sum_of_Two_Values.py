#CSES problem
from collections import defaultdict

n,x = list(map(int,input().split()))
arr = list(map(int,input().split()))
d = defaultdict(lambda : [])
for i in range(n):
    d[arr[i]].append(i+1)
arr.sort()
l = 0
k = 0
r = n-1
while l<=r and k == 0:
    temp =arr[l]+arr[r]
    if temp > x:
        r -= 1
    elif temp < x:
        l += 1
    else:
        k = 1
if k == 1:
    if arr[l] == arr[r]:
        if len(d[arr[l]]) == 1:
            print("IMPOSSIBLE")
        else:
            ind1 = d[arr[l]][0]
            ind2 = d[arr[l]][1]
            print(ind1,ind2)
    else:
        ind1,ind2 = min(d[arr[l]][0],d[arr[r]][0]),max(d[arr[l]][0],d[arr[r]][0])
        print(ind1,ind2)
else:
    print("IMPOSSIBLE") 