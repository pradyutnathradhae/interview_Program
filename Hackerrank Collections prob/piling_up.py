'https://www.hackerrank.com/challenges/piling-up/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen'



from collections import deque

d = deque()
res = []
for _ in range(int(input())):
    n = int(input())
    l = map(int,input().rstrip().split())
    d.extend(l)
    prev = max(d[0],d[n-1])
    flag = 0
    while True:
        if n == 1:
            if d.pop() > prev:
                flag = 1
            break
        else:
            if d[0] >= d[n-1]:
                maxi = d.popleft()
            else:
                maxi = d.pop()
            if maxi > prev:
                flag = 1
                break
            prev = maxi
            n -= 1
    if flag == 0:
        res.append('Yes')
    else:
        res.append('No')
    d.clear()

for i in res:
    print(i)
        
                    
    