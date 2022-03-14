# data => x, y

#behaviour => 
#1 print the coordinates => <2,3>
# 2. print distance between 2 coordinates
# distance between coordinate and origin
#2. Given 3 coordinates => find area of triangle formed
#3. Print line segment => y = mx+b 
#4. Given line and point, find shortest distance between the them
#5. Given line, find distance between the the line and origin
#6. Given line and coordinate, check if the point lies on the line



from cmath import sqrt


class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return "<{},{}>".format(self.x, self.y)

    def euc_distance(self, other):
        dist = ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5
        return dist

    def origin_distance(self):
        return ((self.x)**2 + (self.y)**2)**0.5
