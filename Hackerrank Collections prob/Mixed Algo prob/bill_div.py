'https://www.hackerrank.com/challenges/bon-appetit/problem?h_r=next-challenge&h_v=zen'

def bonAppetit(bill, k, b):
    b_actual = (sum(bill) - bill[k])//2
    if b-b_actual == 0:
        print('Bon Appetit')
    else:
        print(b-b_actual)