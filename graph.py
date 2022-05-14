array = [3,9,2,4,15,10,19]

even =0
odd =0
counter=0
flag=0
def iseven(number):
    if number%2==0:
        return True
    else:
        return False

while(True):
    if counter==len(array)-1 :
        break

    if iseven(array[even])==False and even < len(array)-1:
        even+=1
    if iseven(array[odd])==True and odd<len(array)-1:
        odd+=1




    if iseven(array[even]) and iseven(array[odd])==False:
        print(min(array[even],array[odd]))
        counter+=1
        flag=1
        if array[odd]<array[even] and even < len(array)-1:
            print("odd pointer")
            odd+=1
        elif  odd<len(array)-1:
            print("even pointer")
            even+=1












