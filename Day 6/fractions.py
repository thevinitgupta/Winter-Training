import CG

a = CG.Point(2,3)
b = CG.Point(4,5)
print(a,b)
print(a.euc_distance(b), a.origin_distance() , sep="  ")