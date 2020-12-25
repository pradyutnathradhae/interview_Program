n,m = list(map(int,input().split()))
h = sorted(list(map(int,input().split())),reverse=True)
t_temp = list(map(int,input().split()))
t = []
for i in enumerate(t_temp):
    t.append(i)
t = sorted(t,key = lambda x:x[1],reverse=True)
#print(t)
res = [0]*m
#d = {}
l = 0
for i in range(n):
    if l == m:
        break
    if h[i] <= t[l][1]:
        res[t[l][0]] = h[i]
        l += 1
    else:
        pass
for i in range(m):
    if res[i] == 0:
        res[i] = -1
for i in res:
    print(i)
    


    