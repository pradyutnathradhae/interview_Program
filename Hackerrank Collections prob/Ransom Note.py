'https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps'

from collections import Counter

def checkMagazine(magazine, note):
    #magazine = magazine.rstrip().split()
    #note = note.rstrip().split()
    magazine = Counter(magazine)
    note = Counter(note)
    flag = 0
    for i in note.keys():
        if i in magazine.keys() and magazine[i] >= note[i]:
            pass
        else:
            flag = 1
            break
    if flag == 1:
        return 'No'
    else:
        return 'Yes'