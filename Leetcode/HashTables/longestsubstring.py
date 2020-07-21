def longestsubstring(s):
    dic = {}
    max_length = first_index = current_max = 0
    for index,i in enumerate(s):
        max_length = max(max_length,current_max)
        if i in dic.keys() and dic[i] >= first_index:
            current_max  = index - dic[i]
            first_index = dic[i] + 1
        else:
            current_max += 1
        dic[i] = index
    
    return max(max_length,current_max)

if __name__ == '__main__':
    s = input("Enter the string:")
    print(longestsubstring(s))