'https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays'
'https://www.youtube.com/watch?v=VT-ChOqUsBM'

def swap(l,a,b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp
def minimumBribes(q):
    count = 0
    flag = 0
    for i in range(len(q)-1,1,-1):
        if q[i] == i+1:
            pass
        elif q[i-1] == i+1:
            count += 1
            swap(q,i,i-1)
        elif q[i-2] == i+1:
            count += 2
            swap(q,i,i-2)
            swap(q,i-2,i-1)
        else:
            flag = 1
            break
    if q[0] == 1 and q[1] == 2:
        pass
    else:
        count += 1
        swap(q,0,1)
    if flag == 1:
        print('Too chaotic')
    else:
        print(count)