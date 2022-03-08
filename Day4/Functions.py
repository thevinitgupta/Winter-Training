#abstraction , decomposition

#components : 
#1. def
#2. name
#3.Arguments
#4. Docs
#5. Return

def isEven(n):

    """
    check if a given number is odd or even
    input - any valid +ve integer
    output : true/false

    """
    if n%2 == 0:
        return True
    else:
        return False

for i in range(1,11):
    print(i, "is even : ", isEven(i))