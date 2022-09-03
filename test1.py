number = int(input())
data = list(map(int, input().split()))
days = int(input())

answer = []
answer1 = 0

def function(number,data,days):

    data= sorted(data)
    answer1=-1

    answer = []

    if(days>=number//2):
        days = int(number/2 -1)

    for i in range(len(data)-1):
        answer1=0
        for j in range(i,len(data)-1):
            if data[j]-data[i]>=0 and data[j]-data[i]>answer1:
                answer.append(data[j]-data[i])
                answer1= data[j]-data[i]
    answer= sorted(answer,reverse=True)
    print(answer)
    for i in range(days):
        answer1=answer1+answer[i]
    return answer1



print(function(number,data,days))
