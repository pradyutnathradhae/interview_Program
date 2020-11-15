'https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup'
def countingValleys(steps, path):
    # Write your code here
    d = {
        'U':1,
        'D':-1
    }
    count = 0
    prev = 0
    res = 0
    flag = 0
    for i in range(steps):
        prev = count
        count += d[path[i]]
        if prev == 0 and count < 0:
            flag = 1
        if prev < 0 and count == 0:
            flag = 0
            res += 1
    return res

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    print(result = countingValleys(steps, path))