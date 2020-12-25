def find_sets(n,sumval):
    val = sumval//2
    #print(val)
    s = set(range(1,n+1))
    l = 1
    r = n
    l1 = []
    while val != 0 and l<r:
        if l<=val:
            l1.append(l)
            val -= l
            s.remove(l)
            #print(l)
        
        flag = True
        while flag and r>l:
            if r<=val:
                l1.append(r)
                val -= r
                s.remove(r)
                #print(r)
                flag = False
            r -= 1
        l += 1
        
    l2 = list(s)
    return l1,l2
    #return [1,3,5],[8,9]

n = int(input())
sumval = n*(n+1)//2
if (sumval)%2 == 1:
    print("NO")
else:
    print("YES")
    l1,l2 = find_sets(n,sumval)
    print(len(l1))
    print(" ".join(map(str,sorted(l1))))
    print(len(l2))
    print(" ".join(map(str,sorted(l2))))
    
        