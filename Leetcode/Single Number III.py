def find(nums):
    dic = {}
    l = []
    for i in nums:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    for i in dic.keys():
        if dic[i] == 1:
            l.append(i)
    return l

def find_easy(nums):
    l = []
    for i in nums:
        if i in l:
            l.remove(i)
        else:
            l.append(i)
    return l
if __name__ == '__main__':
    print(find([1, 2, 1, 3, 2, 5]))
    print(find_easy([1, 2, 1, 3, 2, 5]))
