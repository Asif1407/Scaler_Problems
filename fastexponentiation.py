import sys
sys.setrecursionlimit(100000000)


def pow( A, n, p):
    if n==0:
       return 1
    he = pow(A,n/2,p)

    ha = ((he%p) * (he%p)) % p



    if (n%2==0):

        return ha

    else :

        return ((ha%p) * (A%p)) %p


print(pow(2,365,9))
