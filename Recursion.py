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

def printInc(n):
    if n==0 :
        return
    printInc(n-1)
    print(n, end=",")


def printdec( n):
    if n ==1:
        print(1)
        return
    print(n, end =',')
    printdec(n-1)

def recursivepalindrome( string, s, e):
    if s>=e:
        return True
    if (string[s]==string[e]):
        if (recursivepalindrome(string, s+1, e-1)):
            return True
        else:
            return False
    else:
        return False

variable = "globle"
print(recursivepalindrome(variable,0,len(variable)-1))


printdec(7)
