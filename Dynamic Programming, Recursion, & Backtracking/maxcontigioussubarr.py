import math
#O(n^3) Sol_n
def solution1(arr,n):
    maxval = arr[0]
    for i in range(n):
        for j in range(i,n):
            sumval = 0
            for k in range(i,j+1):
                sumval += arr[k]
            if maxval < sumval:
                maxval = sumval 
    print(maxval)   

#O(n^2) Sol_n   
def solution2(arr,n):
    maxval = -math.inf
    for i in range(n):
        sumval = 0
        for j in range(i,n):
            sumval += arr[j]
            if maxval < sumval:
                maxval = sumval 
             
    print(maxval)        
#T = O(n) S= O(n) Sol_n
def solution3(arr,n):
    res = [None]*n
    res[0] = arr[0]
    for i in range(1,n):
        res[i] = max(res[i-1]+arr[i],arr[i])  
    print(max(res))

#T = O(n) S= O(1) Sol_n
#Kadane's Algorithm
def solution4(arr,n):
    maxval = arr[0]
    temp = arr[0]
    for i in range(1,n):
        temp = max(temp+arr[i],arr[i])
        if temp>maxval:
            maxval = temp  
    print(maxval)  

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    solution4(arr,n)
    