'https://www.hackerrank.com/challenges/electronics-shop/problem'

def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards = sorted(keyboards,reverse = True)
    drives  = sorted(drives,reverse = True)
    result = keyboards[-1]+drives[-1]
    if b < (result):
        return -1
    for i in keyboards:
        for j in drives:
            temp =i+j
            if temp<=b and result < temp:
                result = temp
    return result