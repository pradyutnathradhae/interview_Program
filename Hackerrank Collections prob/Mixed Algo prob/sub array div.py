'https://www.hackerrank.com/challenges/the-birthday-bar/problem'

def birthday(s, d, m):
    #square = {1:1,2:4,3:9,4:16,5:25}
    count = 0
    for i in range(len(s)-m+1):
        temp = 0
        for j in range(i,i+m):
            temp += s[j]
        if temp == d:
            count += 1
    #if len(s) == m and sum(s) == d:
    #    count += 1
        
    return count