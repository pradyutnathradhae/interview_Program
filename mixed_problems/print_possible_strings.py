'''Print all possible strings that can be made by placing spaces
Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them.
Input:  str[] = "ABC"
Output: ABC
        AB C
        A BC
        A B C
'''

def place_spaces(st,buf,i,len_str):
    #Just printing the buffer string
    if i==len_str :
        print(buf)
        return 

    #Just copying next character within buf
    buf1 = buf + st[i]
    place_spaces(st,buf1,i+1,len_str)

    #Adding spaces and adding character to buf

    if st[i] != ' ':
        buf2 = buf
        if buf[-1] != ' ':
            buf2 = buf2 + ' '
            buf2 += st[i]
            place_spaces(st,buf2,i+1,len_str)

if __name__ == '__main__':
    st =  input('Enter the string')
    buf = ''
    buf += st[0]
    length = len(st)
    place_spaces(st,buf,1,length)
