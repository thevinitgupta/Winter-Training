import ctypes

class MyList:
    def __init__(self) -> None:
        self.size = 1 #current capacity of list
        self.n = 0 #current no. of items in list
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        #*using the ctype module to make an array of C type with size capacity and returns it
        return (capacity*ctypes.py_object)()

    def __len__(self):
        return self.n

    def append(self,item):
        if self.n==self.size:
            #array is full
            self.__resize(self.size*2)

        #append
        self.A[self.n] = item
        self.n = self.n+1

    def __resize(self,new_capacity):
        #create a new array(double the size)
        B = self.__make_array(new_capacity)
        #copy B to A
        for i in range(self.n):
            B[i] = self.A[i]

        #make B -> A
        self.A = B
        self.size = new_capacity

l = MyList()
print(len(l))
l.append(4)
l.append(1)
l.append(7)
l.append(9)
l.append(0)
print(len(l))