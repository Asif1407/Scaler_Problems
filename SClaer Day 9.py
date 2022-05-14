A = [5, -2, 3 , 1, 2]
B = 4


if B==1:
    print(max(A[0],A[len(A)-1]))
newarray =[]
pf=[0] * (len(A))

max = -999999

for i in range(len(A)-B, len(A)):
    newarray.append(A[i])
for i in range(len(A)-B):
    newarray.append(A[i])

pf[0]=newarray[0]

for i in range(1,len(A)):
    pf[i]= pf[i-1] +newarray[i]


for i in range(B):
    if i+B-1>len(newarray)-1:
        break
    if i == 0:
        sum = pf[B-1]
    else:
        sum = pf[i+B-1]- pf[i-1]
    if sum > max:
        max = sum



    print(sum)
print(max)
print(newarray)
print(pf)


