

array = [1,2,3,4,5,6,7]

def prefix_sum(array):
    pf=[0]*len(array)
    pf[0]=array[0]

    for i in range(1,len(array)):
        pf[i] = pf[i-1]+array[i]

    return pf

print(prefix_sum(array))

