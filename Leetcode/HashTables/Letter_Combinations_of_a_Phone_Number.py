'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''
def newstringlistgen(oldlist,chararray):
    newlist = []
    for i in oldlist:
        for j in chararray:
            newlist.append(i+j)
    return newlist


def lettercombinations(digits):
    dic = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
    st = [i for i in digits]
    if digits == '':
        return []
    ans = [""]
    for i in st:
        ans = newstringlistgen(ans,dic[i])
    
    return ans
  
if __name__ == '__main__':
    print(lettercombinations('23'))  
    print(lettercombinations(''))