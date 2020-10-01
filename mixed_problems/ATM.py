def fun1(arr, inst):
    arr[inst[1] - 1] = inst[2]

def fun2(arr, inst):
    le = -9999999
    for i in range(inst[1]-1, inst[2]):
        if arr[i] % 2 == 0:
            le = max(le, arr[i])
    if le == -9999999:
        return 'DNE'
    return le

def fun2(arr, inst):
    le = -9999999
    for i in range(inst[1]-1, inst[2]):
        if arr[i] % 2 != 0:
            le = max(le, arr[i])
    if le == -9999999:
        return 'DNE'
    return le

n, q = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
while q:
    inst = list(map(int, input().strip().split(' ')))
    if inst[0] == 1:
        fun1(arr, inst)
    elif inst[0] == 2:
        print(fun2(arr, inst))
    elif inst[0] == 3:
        print(fun3(arr, inst))
    q -= 1