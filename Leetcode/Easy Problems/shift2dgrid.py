'''https://leetcode.com/problems/shift-2d-grid/'''
class Solution:
    def shiftGrid(self, grid, k):
        flat = [item for row in grid for item in row]
        lenrow = len(grid[0])
        totalelts = len(flat)
        temp = []
        if totalelts == k:
            return grid
        elif totalelts < k and k % totalelts == 0:
            return grid
        elif totalelts < k and k % totalelts != 0:
            k = k % totalelts
        else:
            pass
        for i in range(len(flat)-k,len(flat),1):
            temp.append(flat[i])
        for i in range(len(flat)-k):
            temp.append(flat[i])
        return [ temp[i:i+lenrow] for i in range(0,len(flat)-lenrow+1,lenrow)]

ob = Solution()
print(ob.shiftGrid([[1,2,3],[4,5,6],[7,8,9]],1))
print(ob.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]],4))