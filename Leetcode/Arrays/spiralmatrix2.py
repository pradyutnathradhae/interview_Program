class Solution:
    def generateMatrix(self, n):
        nums = list(range(1,n*n+1,1))
        # print(nums)
        ind = 0
        direction = 0
        T = 0
        B = n-1
        L = 0
        R = n-1
        if n==1:
            return [[1]]
        res = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(i)
            res.append(temp)
        
        # row = []
        # for i in range(n):
        #     row.append(0)
        # for i in range(n):
        #     res.append(row)
        while T<=B and L <= R:
            # print(T,B,L,R)
            if direction == 0:
                # print(ind,direction)
                for i in range(L,R+1,1):
                    res[T][i] = nums[ind]
                    ind +=1
                T += 1
            elif direction == 1:
                # print(ind,direction)
                for i in range(T,B+1,1):
                    res[i][R] = nums[ind]
                    ind +=1
                R -= 1
            elif direction == 2:
                # print(ind,direction)
                for i in range(R,L-1,-1):
                    res[B][i] = nums[ind]
                    ind +=1
                B -= 1
            else:
                # print(ind,direction)
                for i in range(B,T-1,-1):
                    res[i][L] = nums[ind]
                    ind += 1
                L += 1
            direction = (direction+1)%4
        return res

ob = Solution()
print(ob.generateMatrix(3))              
        
        