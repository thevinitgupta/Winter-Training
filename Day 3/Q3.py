
#l1 = [1,2,[3,4]]
l1 = [[1,2],[3,5]]

l3 = []

for i in l1:
    if(type(i)==list):
        l3.extend(i)
    else :
        l3.append(i)

print(l3)