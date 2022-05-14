

array = [8,2,9]

for i in range(len(array)):
    for j in range(i,len(array)):
        for k in range(i,j+1):
            print(array[k], end=" ")
        print()