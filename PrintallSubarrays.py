

array = [1,2,3,4,5,6,7,8,9]

# for i in range(len(array)):
#     for j in range(i,len(array)):
#         for k in range(i,j+1):
#             print(array[k], end=" ")
#         print()


#subarray sum

for i in range(len(array)):
    for j in range(i,len(array)):
        sum = 0
        for k in range(i,j+1):
            sum = sum + array[k]
            print(array[k], end=" ")
        print()
        print (sum)
        print()
