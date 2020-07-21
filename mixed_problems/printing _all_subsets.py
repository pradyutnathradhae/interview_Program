''''
Power Set
Power Set Power set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.

If S has n elements in it then P(s) will have 2^n elements
'''


def printPowerSet1(arr, n):  #Has O(2^n * n) complexity
    dic = {}
    res = []
    N = int(pow(2,n)) 
    for i in range(len(arr),0,-1):
        temp = int(pow(2,i-1))
        dic[temp] =  arr[i-1]
    #print(dic)
    for i in range(N):
        summed=i
        temp = []
        for j in dic.keys():
            if summed >=j:
                temp.append(dic[j])
                summed = summed - j
            if summed == 0:
                break
        res.append(temp)
    print(res)
    
from itertools import combinations
def printPowerSet2(arr,n):   ##Has O(n^2) complexity
    res = []
    for i in range(n+1):
        for element in combinations(arr,i):
            res.append(list(element))
    print(res)

def printPowerSet3(arr,index,n,current):  #A recursive approach Space: O(2^n)
    if n == index:
        return
    print(current)
    for i in range(index+1,n):
        current.append(arr[i])
        printPowerSet3(arr,i,n,current)
        current.pop()
         

# Driver Code

if __name__ == '__main__': 
    arr = [10, 12, 13] 
    n = len(arr)
    arr.reverse() 
    #print(arr)
    printPowerSet1(arr, n)
    printPowerSet2(arr, n)  
    printPowerSet3(arr,-1,n,[])