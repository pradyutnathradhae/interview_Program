def cal_fact(n):
    fact_val = 1
    for i in range(2,n + 1):
        fact_val *= i
    return fact_val

def cal_trail_zero(res):
    no_zero = 0
    while(True):
        if(res % 10 == 0):
            res //= 10
            no_zero += 1
        else:
            break
    return no_zero

def adv_trailing_zero(res):
    no_zero = 0
    restemp = 5
    while(n // restemp > 0):
        no_zero += res//restemp
        restemp *= 5
    return no_zero
if __name__ == "__main__":
    n = int(input())
    # res = cal_fact(n)
    # no_zero = cal_trail_zero(res)
    no_zero = adv_trailing_zero(n)
    print(no_zero)
