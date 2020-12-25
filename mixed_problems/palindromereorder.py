from collections import Counter
def stringform(s,i):
    st = ''
    for _ in range(i):
        st += s
    return st
st = input().rstrip()
cnt = Counter(st)
s = ''
buff = ''
odd = 0
flag = False
for i in cnt.keys():
    if cnt[i] % 2==1:
        odd += 1
    if odd > 1:
        flag = True
        break
if flag==True:
    print('NO SOLUTION')
elif (len(st)%2==0 and odd==0)or((len(st)%2==1 and odd==1)):
    for i in cnt.keys():
        if cnt[i] %2 != 1:
            s +=stringform(i,cnt[i]//2)
        else:
            buff = i
    if  len(st)%2==0:
        s += s[::-1]
    else:
        s += (stringform(buff,cnt[buff]) + s[::-1]) 
    print(s)        
else:
    print('NO SOLUTION')

###SECOND SOLUTION
n = str(input())
output = ""
odd = 0
odd_char = ""
odd_char_count = 0
for x in range(65, 91):  # capital A-Z
    curr_char = chr(x)
    curr_count = n.count(curr_char)
    if curr_count % 2 == 1:
        odd_char_count = curr_count
        odd += 1
        if odd > 1:
            print("NO SOLUTION")
            exit(0)
        odd_char = curr_char
        # print("Odd:", curr_char)
    else:
        output += curr_char * (curr_count//2)
if odd_char:
    output += odd_char*odd_char_count
    output += output[::-1][odd_char_count:]
else:
    output += output[::-1]
print(output)