def subsets(li):
    subs = []
    subs.append([])
    return extend(subs,li,0)

def extend(subs,li,i):
    if i>= len(li):
        return subs
    n = []
    for l in subs:
       copy = l[:]
       copy.append(li[i]) 
       n.append(l)
       n.append(copy)
    return extend(n,li,i+1)

arr = [1,2,3,4]
print(sorted(subsets(arr)))

