
# default values for arguments
def power(a=1,b=1):
    return a**b

print(power(2,3))
print(power(2))
print(power())


print(power(b=2,a=3))

#! arbitary arguments
def sum(*num):
    res = 0
    print(type(num)) #tuple
    for i in num:
        res += i
    return res

print(sum(1,2))
print(sum(1,2,3,4,5,6,7))