A = [ 15, 7, 11, 7, 9, 8, 18, 1, 16, 18, 6, 1, 1, 4, 18 ]
B = 6
j = B-1
sum =0
ans = 100000000000000000
for i in range(B):
    sum = sum + A[i]
if sum < ans :
    ans = sum
    counter=0

print(sum)

for i in range(len(A)-j-1):
    sum = sum - A[i]+A[i+j+1]
    print(sum)
    if sum<ans:
        print("i=", i+1)
        ans = sum

