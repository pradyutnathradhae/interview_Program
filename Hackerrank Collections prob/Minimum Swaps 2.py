'https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays'

def minimumSwaps(arr):
    index = {}
    arr_sort = sorted(arr)
    swap_count = 0
    for i in range(len(arr)):
        index[arr[i]] = i
    for i in range(len(arr)):
        if arr_sort[i] == arr[i]:
            pass
        else:
            a = index[arr_sort[i]]
            temp = arr[a]
            arr[a] = arr[i]
            arr[i] = temp
            index[arr[a]] = a
            swap_count += 1
    return swap_count