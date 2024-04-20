

array = [5,4,3,2,1]




def selection_sort(array):
    print("Sorting Array using selection sort")
    for i in range(len(array)):
        min = i
        for j in range(i, len(array)):
            if array[j]<array[min]:
                min=j
        temp = array[i]
        array[i]= array[min]
        array[min]=temp
        print("Swap "+ str(i) )
        print(array)

def bubble_sort(array):

    print("Sorting using bubble sort")

    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j]= array[j+1]
                array[j+1] = temp
        print("Swap" + str(i))
        print(array)


def insertion_sort(array):

    print("Sorting using insertion sort")









selection_sort([5,4,3,2,1])

bubble_sort([5,4,3,2,1])



