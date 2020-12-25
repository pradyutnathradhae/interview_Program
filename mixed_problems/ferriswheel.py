n,x = list(map(int,input().split()))
arr = sorted(list(map(int,input().split())),reverse=True)
l = 0
count = 0
r = len(arr)-1
while l<=r:
    if arr[l] + arr[r] <=x:
        r -= 1
    l += 1
    count += 1

print(count)
        
        