'https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays'

def hourglassSum(arr):
    maxval = -math.inf
    for i in range(4):
        for j in range(4):
            val = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            maxval = max(maxval,val)
    
    return maxval