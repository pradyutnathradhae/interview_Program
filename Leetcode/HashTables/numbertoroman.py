def intToRoman(num):
    dic = {
        1:'I',
        2:'II',
        3:'III',
        4:'IV',
        5:'V',
        6:'VI',
        7:'VII',
        8:'VIII',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90:'XC',
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M'
    }
    res = []
    key = list(dic.keys())
    key.reverse()
    print(key)
    i = 0
    while num>0:
        flag = 0
        while flag == 0 and i < len(key):
            if key[i] <= num:
                num = num - key[i]
                res.append(dic[key[i]])
                flag = 1
            else:
                i = i + 1
    
    return ''.join(res)

if __name__ == '__main__':
    print(intToRoman(1994))