
#https://leetcode.com/problems/decode-string/

def decodeString(s):
        '''Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
        '''
        stack1 = []
        stack2 = []
        num = 0
        resstr = ''
        def genstr(ch,freq):
            return ch*freq
        for i in s:
            if i.isnumeric():
                num = (num*10)+int(i)
            elif i == '[':
                stack1.append(num)
                num = 0
                stack2.append(i)
            elif i == ']':
                poped = stack2.pop()
                temp = ''
                while poped != '[':
                    temp = poped + temp
                    poped = stack2.pop()
                temp = genstr(temp,stack1.pop())
                stack2.append(temp)
            else:
                stack2.append(i)
        for i in stack2:
            resstr += i
        return resstr
    
if __name__ == "__main__":
    print(decodeString("2[abc]3[cd]ef"))