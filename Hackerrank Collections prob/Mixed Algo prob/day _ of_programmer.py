'https://www.hackerrank.com/challenges/day-of-the-programmer/problem'

def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    elif year < 1918:
        if year % 4 == 0:
            temp = '12.09.'+str(year)
        else:
            temp = '13.09.'+str(year)
        return temp
    else:
        flag = 0
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            flag = 1
        if flag == 1:
            temp = '12.09.'+str(year)
        else:
            temp = '13.09.'+str(year)
        return temp