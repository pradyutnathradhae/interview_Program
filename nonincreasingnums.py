def numofnonincreasing(n):
    length = len(str(n))
    res = 0
    if length == 1:
        return n+1
    else:
        res = 10
        for i in range(10,n+1):
            temp = i
            d = -1
            while temp != 0:
                if (temp %10) >= d:
                    d = temp %10
                    temp = temp //10
                else:
                    break
            if temp == 0:
                res += 1
        return res
                    
    
    
n = int(input())
print(numofnonincreasing(n))

