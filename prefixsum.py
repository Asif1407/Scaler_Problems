#https://www.scaler.com/academy/mentee-dashboard/class/24920/assignment/problems/298?navref=cl_tt_nv

A = [5, 6, -1, 7, 8,8,8,8,8,8,8,8,8]

pf = [0] * len(A)
pf[0] =A[0]

for i in range(1,len(A)):
    pf[i] = pf[i-1]+ A[i]


print(pf)