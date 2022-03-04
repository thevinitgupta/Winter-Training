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


l1=[1,2,3,4]
l1[1:2] = [100,200,300]
print(l1)
l1.append(600) # add 1 element
l1.extend([101,202,303]) #append multiple values
print(l1)

l1.append([10001,10101])  #!always adds only 1 value in the end
print(l1)

l1.extend('goa') #!append 'g', 'o' and 'a' separately -> always adds mutiple values
print(l1)

l1.insert(1,150)
print(l1)


