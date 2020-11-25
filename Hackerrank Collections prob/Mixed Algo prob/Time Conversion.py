def aligntime(minu,sec):
    minu += (sec //60)
    sec = sec % 60
    hour = minu // 60
    minu = minu % 60
    return hour,minu,sec
def jointime(arr):
    st = ''
    for i in range(3):
        s = str(arr[i])
        #print(s)
        if len(s) == 1:
            s = '0' + s
        arr[i] = s
    st = ':'.join(arr)
    return st
    
def timeConversion(s):
    #
    # Write your code here.
    #
    strs = s.split(':')
    hour = int(strs[0])
    minu = int(strs[1])
    sec = int(strs[2][:-2])
    merid = strs[-1][-2:]
    temp_hour,minu,sec = aligntime(minu,sec)
    #print(temp_hour,minu,sec)
    if merid == 'PM' or (hour != 12 and (hour + temp_hour) >= 12):
        if hour == 12:
            hour += temp_hour
        else:
            hour += 12 + temp_hour
    else:
        
        if hour == 12:
            hour = 0
        hour += temp_hour
    #print(hour,minu,sec)
    s = jointime([hour,minu,sec])
    return s

if __name__ == "__main__":
    s = input()
    print(timeConversion(s))
    	