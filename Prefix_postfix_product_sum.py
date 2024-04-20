

array=[1,2,3,4]


prefix = [None] * (len(array))
# print(prefix)

#calculate the prefix multiply array
prefix[0]=array[0]

for i in range(1,len(array)):
    prefix[i]=prefix[i-1]*array[i]

print(prefix)
print(array)


#calculate the post fix multiple array
postfix=[None]*len(array)
postfix[len(array)-1]= array[len(array)-1]

for i in reversed(range(len(array)-1)):
    #print(i)
    postfix[i]=postfix[i+1]*array[i]
print(postfix)

for i in range(len(array)):
    if i ==0:
        print(postfix[i+1])
    elif i ==(len(array)-1):
        print(prefix[i-1])
    else:
        print(postfix[i+1]*prefix[i-1])


