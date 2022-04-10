

def calculate(length):
    if length  == 2:
        return ['00','01','11','10']
    else:
        l1 = calculate(length-1)
        l2 = l1[::-1]
        l1_temp = ['0'+x for x in l1]
        l2_temp = ['1'+x for x in l2]
        l1_temp.extend(l2_temp)
        return l1_temp

if __name__ == '__main__':
    n = int(input())
    if n==1:
        print('0\n1')
    else:
        l = calculate(n)
        print('\n'.join(l))