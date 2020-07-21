'''
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''


def maxArea(height):
    max_area = 0
    l = 0
    r = len(height) - 1
    while l < r:
        max_area = max(max_area,(r-l)*min(height[l],height[r]))
        if height[l] > height[r]:
            r = r - 1
        else:
            l = l + 1
    return max_area

def maxAreaNaive(height):  #A Naiive Approach
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1,len(height)):
            max_area = max(max_area,(j-i)*min(height[i],height[j]))
    return max_area

if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))