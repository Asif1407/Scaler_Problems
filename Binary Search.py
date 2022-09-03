

def binarysearch( array, target):
    l = 0
    r = len(array)-1


    while(l<=r):
        mid = int((r+l)/2)
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            #reject the left half
            l = mid + 1
        else:
            # reject the right half
            r= mid -1
    return -1

array = list(map(int, input().split()))

print(binarysearch(array, 24))