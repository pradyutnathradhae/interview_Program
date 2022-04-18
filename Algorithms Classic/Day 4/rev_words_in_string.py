'''https://leetcode.com/problems/reverse-words-in-a-string-iii/'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words= s.split(" ")
        for i in range(len(words)):
            li = [x for x in words[i]]
            l = 0
            r = len(li)-1
            while l<= r:
                temp = li[l]
                li[l] = li[r]
                li[r] = temp
                l += 1
                r -= 1
            words[i] = "".join(li)
        return " ".join(words)