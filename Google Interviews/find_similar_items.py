'''Given an array of n elements which contains elements from 0 to n-1, 
with any of these numbers appearing any number of times. Find these repeating numbers in O(n) 
and using only constant memory space.
'''
#Added a special feature to find the no. of repeat in repeated elements

def find_repeated_item_freq(arr,n):
    count = []
    for i in range(0,n):
        count.append(0)
    for i in arr:
        count[i] += 1
    for i in range(0,n):
        if count[i] > 1:
            print(str(i) +" has occured " + str(count[i]) + " times")

def find_repeated_item(arr,n):
    for i in range(0, n):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -1 * arr[abs(arr[i])]
        else:
            print(abs(arr[i]))

if __name__ == '__main__':
    find_repeated_item([1, 2, 3, 3, 2], 5)
    find_repeated_item_freq([1,2,3,3,2,2],6)
