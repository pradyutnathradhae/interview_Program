from collections import defaultdict,Counter
# Complete the freqQuery function below.
def freqQuery(queries):
    arr = defaultdict()
    res = []
    for i in queries:
        if i[0] == 1:
            if i[1] in arr:
                arr[i[1]] += 1
            else:
                arr[i[1]] = 1
        elif i[0] == 2:
            if i[1] in arr:
                arr[i[1]] -= 1
                if arr[i[1]] == 0:
                    arr.pop(i[1])
        else:
            if i[1] in arr.values():
                res.append(1)
            else:
                res.append(0)
    
    return res

def freq(queries):
    freq = Counter()

    cnt = Counter()

    arr = []

    for q in queries:
        if q[0]==1:
            cnt[freq[q[1]]]-=1
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1

        elif q[0]==2:
            if freq[q[1]]>0:
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                cnt[freq[q[1]]]+=1

        else:
            if cnt[q[1]]>0:
                arr.append(1)
            else:
                arr.append(0)

    return arr