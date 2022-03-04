#dictionary
#! Dictionary is mutable
#* no indexing/slicing
#? keys are not mutable
#todo keys cannot be repeated

d1 = {"name" : "Vinit","Age" : 21, "gender" : "male"}
print(d1)

d2 = {}
print(d2)

d3 = {
    "name" : "Vinit",
    "Age" : 21, 
    "marks" : {
        "Phy" : 95,
        "Computer" : 100,
        "Maths" : 73
    }
}

print(d3)

print({"name" : "Vaibhav", "name" : "Vinit"})

#accessing
#* accessed using keys

print(d3['marks']['Phy']) 

#? adding new key-value pair
d3['college']='hit'
print(d3)


del d3['college']
print(d3)

#* loops and membership operations are only Applicable

#* methods applicable -> len, max, min , sorted, keys, values
print(len(d3))

print(d3.keys())
print(d3.values())