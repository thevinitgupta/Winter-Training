#multiplication using recursion
def prod(n,m):
    if(m==1):
        return n
    return prod(n,m-1)

# 1. Factorial using recursion
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

print(fact(6))

# 2. Palindrome or not
def isPalin(s):
    if len(s)<=1:
        return True
    # madam
    elif s[0]==s[-1]:
        return isPalin(s[1:-1])
    else:
        return False

print(isPalin("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"))

