'''
Case-specific sorting of Strings in O(n) time and O(n) space
Given a string str consisting of uppercase and lowercase characters. The task is to sort uppercase and lowercase characters separately such that if the ith place in the original string had an uppercase character then it should not have a lowercase character after being sorted and vice versa.

Examples:

Input: str = “gEeksfOrgEEkS”
Output: eEfggkEkrEOsS

Input: str = “eDefSR”
Output: eDefRS
'''

def sorting(s,n):
    lower = []
    upper = []
    for i in s:
        if i > 'a' and i < 'z':
            lower.append(i)
        if i > 'A' and i < 'Z':
            upper.append(i)
    
    upper = sorted(upper)
    lower = sorted(lower)
    i=0
    j=0
    s=[i for i in s]
    for k in range(n):
        if s[k] > 'a' and s[k] < 'z':
            s[k] = lower[i]
            i += 1
        if s[k] > 'A' and s[k] < 'Z':
            s[k] = upper[j]
            j += 1
    
    return "".join(s)

if __name__ == '__main__':
    print(sorting('gEeksfOrgEEkS',len('gEeksfOrgEEkS')))
