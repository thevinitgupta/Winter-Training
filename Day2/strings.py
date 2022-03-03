city = "haldia"
print(city)
city = 'haldia'
print(city)
city="It's a rainy day"
print(city)

city="""Hello,
    How are you?""" #! like string literals in javascript
print(city)
city='haldia'
#!indexing
print(city[5]) #? accessing characters, works with negative values too

#! slicing
print(city[2:5])
print(city[2:])
print(city[ : 6]) #? upto 5 index
print(city[:]) #!whole
print(city[1:10 : 2]) #todo -> specify skips
print(city[2::2])
print(city[:3:2])
print(city[::-1]) #!reversing a string


#!strings are mutable

#* del -> delete variable
del city

#? output -> NameError: name 'city' is not defined
#* print(city) 



city1 = 'Delhi'
city2 = 'Pune'
print(city1+city2)
print(city1*4)

#! invalid statements
#print(city1-city2)
#print(city2/city1)

print(city1>city2) #todo -> only compares with ascii values and not on length

print('de' in city1)

for i in city1:
    print(city2)



#* functions in strings

city = 'kolkata'

#! len, min/max, sorted (available for strings, list, dictionaries)
print(len(city))
print(min(city))
print(max(city))
print(sorted(city)) #ascending
print(sorted(city,reverse=True)) #descending

#? only available in strings
print("My name is Khan".title())
print("My name is Khan".count('is'))
print("My name is Khan".find('is'))

print(" dvsd sdgds ".strip()) #? works like trime in java
print("Vinit Gupta".replace("i","a"))

#!important
print('My name is {} my age is {}'.format("Vinit", 21))
print('My name is {1} my age is {0}, I love {2}'.format(21,"Basketball","Vinit"))
print('My name is {2} my age is {0}, I love {2}'.format(21,"Basketball","Vinit"))
# ! throws error as 3 is out of bounds -> print('My name is {3} my age is {0}, I love {2}'.format(21,"Basketball","Vinit"))

