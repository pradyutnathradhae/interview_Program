n = int(input())
res = []
for _ in range(n):
    a,b = list(map(int,input().split()))
    
    a,b = (a,b) if a>b else (b,a)
    if 2*b<a:
        res.append('NO')
    else:
        a %=3
        b %=3
        a,b = (a,b) if a>b else (b,a)
        if (a==2 and b==1)or(a==b and b==0):
            res.append('YES')
        else:
            res.append('NO')

for i in res:
    print(i)