def recursivesum(N):

    if N==1:
        return 1
    return recursivesum(N-1)+N

def recursivefactorial(n):
    if n==0 or n==1:
        return 1
    return n* recursivefactorial(n-1)


def fibonacci(n):
    if n == 1 or n ==2 :
        return 1
    return fibonacci(n-1) + fibonacci(n-1)


print(fibonacci(5))
print(recursivefactorial(4))
print(recursivesum(100))
