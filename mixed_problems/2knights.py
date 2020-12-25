'https://www.youtube.com/watch?v=h_m12v6SMeY'

def calc(n):
    return ((n**2)*(n*n - 1) - 8 - 24 - (n-4)*16 - 16 - 24*(n-4) - 8*(n-4)*(n-4))//2

n = int(input())
for i in range(1,n+1):
    print(calc(i))