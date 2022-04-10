def main():

    # Write code here
    virus = input()
    res = {True:'POSITIVE',False:'NEGATIVE'}
    for i in range(int(input())):
        sample = input()
        i,j=0,0
        m,n=len(virus),len(sample)
        while i < m and j <n:
            if virus[i] == sample[j]:
                j += 1
            i += 1
        print(res[j==n])



main()