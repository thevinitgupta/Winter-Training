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
