'https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem'

def rankdetermine(x,ranked):
    l = 0
    u = len(ranked)-1
    k = 0
    while l <= u:
        mid = (l+u)//2
        if ranked[mid] > x and ranked[mid+1] < x:
            k = mid+1
            break
        elif ranked[mid] > x and ranked[mid+1] > x:
            l = mid +1
        else:
            u = mid - 1
    return k
        
                   
    
    
    
def climbingLeaderboard(ranked, player):
    res = []
    ranked = list(set(ranked))
    di = {}
    c = 0 
    ranked = sorted(ranked,reverse = True)
    for i in range(len(ranked)):
        di[ranked[i]] = i + 1    
    for i in player:
        if i in di.keys():
            res.append(di[i])
        elif i > ranked[0]:
            res.append(1)
        elif i < ranked[-1]:
            res.append(len(ranked)+1)
        else:
            res.append(rankdetermine(i,ranked)+1)
    return res
        
if __name__ == "__main__":
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    print(result) 
      
    