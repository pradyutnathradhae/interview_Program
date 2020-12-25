def mindiff(arr,n):
    total = sum(arr)
    minval = total
    for i in range(pow(2,n)):
        temp = 0
        bn = bin(i)[2:]
        for j in range(len(bn)):
            if bn[j] == '1':
                temp += arr[n - (len(bn)-j)]
        minval = min(minval,abs(total-(2*temp)))
    return minval

n = int(input())
ls = sorted(int(i) for i in input().split())

s = sum(ls)

def minimum(s, ls):
    if len(ls) == 1:
        return abs(s - 2*ls[0])
    else:
        m =abs(s - 2*ls[0])
        for i in range(1,len(ls)):
            m = min(m,abs(minimum(s - 2*ls[i], ls[:i])))
        return m

print(minimum(s,ls))
                
                
        
    
    

#n = int(input())
#arr = list(map(int,input().split()))
#arr = sorted(arr)
#print(mindiff(arr,n))