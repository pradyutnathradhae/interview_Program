# Karatsuba's Algorithm
# when n is a power of 2

def multiply(x,y,n):
    if n == 1:
        return int(x)*int(y)
    a = x[:n//2]
    b = x[n//2:]
    c = y[:n//2]
    d = y[n//2:]
    return (pow(10,n)*multiply(a,c,n//2)) + (pow(10,n//2)*(multiply(a,d,n//2)+multiply(b,c,n//2))) + multiply(b,d,n//2)


if __name__ == "__main__":
    print(multiply('1234','9876',4))
    