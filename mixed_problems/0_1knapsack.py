'''
Problem Statement-:  You have M questions and N seconds to complete a test. Each question has some points and takes some time to solve (which will be given as input). Find the maximum mark that can be scored by the student within the given time N.

Sample test case:

4 // number of questions
10 // Total time to attend the test
1 2 // one mark question – 2 seconds to solve.
2 3 // two mark question – 3 seconds to solve.
3 5 // three mark question – 5 seconds to solve.
4 7 // 4 mark question – 7 seconds to solve.
'''

n = int(input())
T = int(input())
arr = []
for i in range(n):
    point,time = list(map(int,input().split()))
    arr.append([point,time])
arr.sort(key=lambda x:x[0],reverse=True)

k = [ [0 for j in range(T+1)] for i in range(n+1)]

for i in range(n+1):
    for j in range(T+1):
        if i==0 or j == 0:
            k[i][j] = 0
        elif arr[i-1][1] <= j:
            k[i][j] = max(k[i-1][j],arr[i-1][0]+k[i-1][j-arr[i-1][1]])
        else:
            k[i][j] = k[i-1][j]
print(k[n][T]) 
    