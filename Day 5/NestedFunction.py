def f():
    print("Inside F")
    def g():
        print("Inside G")
    return g()

print(f.__name__)
a = [1,2,3,f]
print(a)
f.__name__="Vinit"
f.val = 34
print(f.__name__)
print(a)
print(f.val)


# callbacks
def power(x,a,b):
    return x(a)**b

def y(x):
    return x**2

print(power(y,2,3))