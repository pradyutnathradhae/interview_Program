


forbid = []
for i in range(8):
    s = input().rstrip()
    for j in range(8):
        if s[j] == '*':
            forbid.append([i,j])
k = 0
def isvalid(rowplacements):
    lastrow = len(rowplacements)-1
    for i in range(lastrow):
        diff = abs(rowplacements[i]-rowplacements[lastrow])
        if diff == 0 or diff == lastrow-i:
            return False
    return True

def isunreserved(i,j):
    for x in forbid:
        if x[0] == i and x[1] == j:
            return False
    return True

def placequeen(row,rowplacements):
    if row == 8:
        global k
        k += 1
    else:
        for col in range(8):
            rowplacements.append(col)
            if isvalid(rowplacements) and isunreserved(row,col):
                placequeen(row+1,rowplacements)
            rowplacements.pop()

placequeen(0,[])
print(k)
        
        
        
    
            

            