

array = [1,2,3,4,5]

def reverse(array,m,n):
    if m == n:
        return
    else :
        temp =array[m]
        array[m]=array[n]
        array[n]= temp
        reverse(array,m+1, n-1)
reverse(array,0,4)
print(array)
print(array)