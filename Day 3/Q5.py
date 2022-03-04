inp = input("Enter a number : ")

num = list(inp)
num1 = list(set(num))

if len(num)!=len(num1):
    print("Yes")
else:
    print("No")