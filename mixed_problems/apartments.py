n,m,k = list(map(int,input().split()))

a = sorted(list(map(int,input().split())),reverse=True)
reqd,avail = 0,0
b = sorted(list(map(int,input().split())),reverse=True)
count = 0

while(reqd<n and avail <m):
    if abs(a[reqd]-b[avail])<=k:
        count += 1
        avail += 1
        reqd += 1
    elif a[reqd] - b[avail] > k:
        reqd += 1
    else:
        avail += 1
    
print(count)