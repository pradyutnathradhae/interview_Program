'''
Power Set in Lexicographic order
This article is about generating Power set in lexicographical order.

Examples :

Input : abc
Output : a ab abc ac b bc c
'''
def powersetgen(s,index,n,current):
    if index == n:
        return
    if len(current) > 0:
        print(current)
    for i in range(index+1,n):
        current += s[i]
        powersetgen(s,i,n,current)
        current = current[:len(current) - 1]
        
if __name__ == '__main__':
    a = input("Enter the string")
    a = ''.join(sorted(a))
    
    powersetgen(a,-1,len(a),"")