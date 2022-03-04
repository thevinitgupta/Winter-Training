#create, access, edit, add, delete, ops, functions

#!slower than normal arrays
l1 = [1,2,3,4] #*homogenous list (same data type)
print(l1)

l1 = [1,False,"Vinit",156.6] #*heterogenous
print(l1)

l1 = []#empty

l1 = [1,2,3,[3,34,3]] #? hetero genous multi dimensional list
print(l1)

l1 = [[[1,2],[3,4]],[[5,6],[7,8]]] #* homo genous 3D list
l1 = 'goa'

l1 = list() #empty list

print(l1)

l1 = [1,2,3,4] #*homogenous list (same data type)
print(l1[0])
print(l1[-1])
print(l1[::-1])

l1 = [1,2,3,[3,34,6]] #? hetero genous multi dimensional list
print(l1[-1][-1])


l1 = [[[1,2],[3,4]],[[5,6],[7,8]]] #* homo genous 3D list
print(l1[1][1][0])
print(l1[-2][-1][-2])