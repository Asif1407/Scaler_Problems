


customers  = [["abc","xcd","xyz"],["abc","bnm","klm"],["abc","scd","dfd"]]
def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j] > sub_li[j + 1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
            if (sub_li[j] == sub_li[j + 1]):

                if (sub_li[j][1] > sub_li[j + 1][1]):
                    tempo = sub_li[j]
                    sub_li[j] = sub_li[j + 1]
                    sub_li[j + 1] = tempo
    return sub_li

print(Sort(customers))


def binarySearch(arr, left, right, x):
    if right >= left:
        middle = left + (right - left) // 2
        if arr[middle] == x:
            return middle
        elif arr[middle] > x:
            return binarySearch(arr, left, middle - 1, x)
        else:
            return binarySearch(arr, middle + 1, right, x)
    else:
        return False

array1=[1,2,3,4,5,6,7,8,9]
print(binarySearch(array1,0,len(array1)-1,23))
