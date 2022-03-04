#cousins of lists
t1 = (1,2,3,4,5) #homo

t2 = (1,2,2.5,True,False) #hetero

t3 = (1,2,3,(4,5,6)) #2D tuple

#!We cannot create single valued tuple directly
t4 = (1,) #* this is correct

t5 = tuple('goa')

print(t2,t2,t3,t4,t5, sep='\n')
