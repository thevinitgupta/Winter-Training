l1 = [1,2,3,2,4,1,3]

# l1 = list(set(l1))
# print(l1)

O = []
for i in l1:
    if i not in O:
        O.append(i)

print(O)