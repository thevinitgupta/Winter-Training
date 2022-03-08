# list stores memoery refernces of the values
#and 2D lists stores the reference of the inner list

# if the data tye used is immutable, when we update that variable, the memory reference changes
# 
# 
a = [1,2,3]
b = list(a) #cloning to prevent errors due to mutability
print(id(a))
print(id(b)) 

