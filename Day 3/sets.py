#Rules of sets
#* Sets are MUTABLE
#! Sets CANNOT have MUTABLE DATA TYPE elements
#? Sets can't have Duplicate values
#todo There are no concepts of Indexing or slicing

#creation
s1 = {1,2,3,4} #homo genous
print(s1)

s2 = {True, "Vinit", 3}
print(s2)

#process of creating empty sets
s3 = set()

s4 = {1,2,3,4,2,3}
print(s4)

s5 = {1,2,3,(2,3)}
print(s5)

#! cannot access elements using indexing

#!cannot edit but can append
s1.add(10)
print(s1)

del s4

#! here POP removes from the first
print(s1.pop())

print(s1.remove(4))


#operations on set
#!union
print(s1 | s2)

#* intersection
print(s1 & s2)

#? set difference
print(s1-s2)

#loop and membership works


#methods
print(len(s1))
print(max(s1),min(s1),sorted(s1))

print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))