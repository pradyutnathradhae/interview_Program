def minus(val):
    if val == 0:
        return 1
    else:
        return 3
def jumpingOnClouds(c, k):
    i = 0
    n = len(c)
    e = 100
    #e -= minus(c[0])
    flag = 0
    while flag == 0:
        i = (i+k)%n
        print(i)
        if i == 0:
            flag = 1
        e -= minus(c[i])
        print(e)
    
    #e -= minus(c[0])
    return e

if __name__ == "__main__":
    print(jumpingOnClouds([0,0,1,0,0,1,1,0],2))