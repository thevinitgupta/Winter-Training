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

print(isPalin("madama"))

# 3. Print powers of 2 upto but not including given number
# bottom up
def powers(n):
    getPowers(n,0)

def getPowers(x,i):
    if 2**i >= x:
        return
    print(2**i)
    getPowers(x,i+1)

#top down
def powersLess(n):
    if n==1:
        print(1)
        return 1
    res = powersLess(n//2)
    print(res*2)
    return res*2

powersLess(63)

#powers(32)
# 
# 4 Fibonacci
 
