def extravalcalc(row,col,maxmat):
    val = 0
    modval = (maxmat) % 2
    if row == col:
        return row
    elif row > col and modval == 1:
        return col
    elif row > col and modval == 0:
        return row+(row-col)
    elif row < col and modval == 0:
        return row
    else:
        return col+(col-row)
        
     
    pass
res = []
t = int(input())
for i in range(t):
    row,col = list(map(int,input().split()))
    maxmat = max(row,col)
    val = (maxmat-1)**2 + extravalcalc(row,col,maxmat)
    res.append(val)

for i in range(t):
    print(res[i])

    
    
    