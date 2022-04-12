'''https://leetcode.com/problems/game-of-life/'''  #- Medium Level Problem

'''[2nd bit, 1st bit] = [next state, current state]

- 00  dead (next) <- dead (current)
- 01  dead (next) <- live (current)  
- 10  live (next) <- dead (current)  
- 11  live (next) <- live (current) '''

class Solution:
    def countlives(self,board,m,n,i,j):
        count = 0
        for a in range(max(i-1,0),min(i+1,m-1)+1,1):
            for b in range(max(j-1,0),min(j+1,n-1)+1,1):
                count += board[a][b] & 1
        count -= board[i][j] & 1
        return count

    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if board == None or len(board) == 0:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                liveno = self.countlives(board,m,n,i,j)
                if board[i][j] == 1 and liveno >= 2 and liveno <= 3:
                    board[i][j] = 3
                if board[i][j] == 0 and liveno == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1