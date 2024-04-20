# https://www.scaler.com/academy/mentee-dashboard/class/24912/assignment/problems/4256?navref=cl_tt_lst_sl

A = "111011101"
A=list(map(int,A))
n=(len(A))

count=0
flag=1
ans=[0]
for i in range(n):
    if A[i]==1:
        count+=1
    if A[i]==0 and flag == 1:
        count +=1

        flag =0
        continue

    if A[i]==0 and flag == 0:
        ans.append(count)
        count=0
        flag=1
print(max(ans))