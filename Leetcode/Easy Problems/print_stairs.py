def recurse(total,curr,l):
    if total == curr:
        st = ' + '.join(l)
        print(st)
        return
    if total >= curr+1:
        l1 = l.copy()
        l1.append('1 step')
        recurse(total,curr+1,l1)
    if total >= curr+2:
        l2 = l.copy()
        l2.append('2 steps')
        recurse(total,curr+2,l2)
def climbStairs(n):
    recurse(n,0,[])
    
    
if __name__ == "__main__":
    n = int(input())
    climbStairs(n)
    