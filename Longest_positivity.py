# https://www.scaler.com/academy/mentee-dashboard/class/24912/homework/problems/8515?navref=cl_tt_lst_sl

A = [5, 6, -1, 7, 8,8,8,8,8,8,8,8,8]

count = 0
for i in range(len(A)):
    if A[i]>=0:
        count+=1
        s=i
        
    if A[i]<0:
        count=0
print(count)