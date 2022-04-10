# Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. 

# This is a famous Google interview question, also being asked by many other companies now a days.
'''Consider the following dictionary 
{ i, like, sam, sung, samsung, mobile, ice, 
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes 
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" 
or "i like sam sung".'''

def wordBreak(words_dictionary,word):
    if word == '':
        return True
    wordlen = len(word)
    return any([(word[:i] in words_dictionary) and wordBreak(words_dictionary,word[i:]) for i in range(1,wordlen+1)])
xx=wordBreak(['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 
  'cream', 'icecream', 'man','go', 'mango'],'ilikesamsamsungmobile')
print(xx)