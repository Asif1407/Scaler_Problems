
numbers=[2,7,11,15]
target = 9

leftpointer=0
rightpointer=len(numbers)-1
sum=None

while sum!=target:
    sum = numbers[leftpointer]+numbers[rightpointer]
    if sum > target:
        rightpointer -=1
    if sum<target:
        leftpointer +=1

answer=[leftpointer+1,rightpointer+1]

print(answer)

