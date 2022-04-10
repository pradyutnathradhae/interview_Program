#https://leetcode.com/problems/single-number-ii/

def singleNumber(nums):
    temp = set(nums)
    return (3*sum(temp) - sum(nums)) // 2

if __name__ == '__main__':
    print(singleNumber([0,1,0,1,0,1,99]))