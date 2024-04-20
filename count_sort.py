

arr=list(map(int,input().split()))
print(len(arr))

# Write your code here
# print(len(set(arr)))
maximum = max(arr)
print(maximum)
frequncy = [0]*(maximum+1)

for i in range(len(arr)):
    frequncy[arr[i]]+=1
print(len(frequncy))
print(frequncy)


