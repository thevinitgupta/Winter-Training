import ctypes

class MyList:
    def __init__(self) -> None:
        self.size = 1 #current capacity of list
        self.n = 0 #current no. of items in list
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        #*using the ctype module to make an array of C type with size capacity and returns it
        return (capacity*ctypes.py_object)()

    def __str__(self) -> str:
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i])+','

        return '['+result[:-1]+']'

    def __getitem__(self,index):
        if 0<= index< self.n:
            return self.A[index]

        else:
            return 'IndexError'


    def __len__(self):
        return self.n

    def append(self,item):
        if self.n==self.size:
            #array is full
            self.__resize(self.size*2)

        #append
        self.A[self.n] = item
        self.n = self.n+1

    def pop(self):
        if self.n==0:
            print('EmptyList')
        else:
            print(self.A[self.n-1])
            self.n = self.n-1

    def clear(self):
        self.n = 0

    def index(self,item):
        for i in range(self.n):
            if type(self.A[i])== type(item) and self.A[i]==item:
                return i

        return 'ValueError - Not in List'

    def insert(self, index, element):
        if self.n==self.size:
            self.__resize(self.n*2)
        
        for i in range(self.n,index,-1):
            self.A[i] = self.A[i-1]
        self.A[index] = element
        self.n = self.n+1

    def __delitem__(self, index):
        if 0 <= index < self.n:
            for i in range(index, self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n-1

        else:
            print('IndexError')        

    def remove(self, element):
        for i in range(self.n):
            if self.A[i]==element:
                self.__delitem__(i)
                return
        print('ValueError - Not in List')   
        

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
l.append(1)
l.append("hello")
l.append(7)
l.append(True)
l.append(None)
print(len(l))
print(l)
print(l[4])
print(l[6])
l.pop()
# l.pop()
# l.pop()
# print(l)
# l.clear()
# print(l)
# l.pop()
# l.pop()
# l.pop()
# print(l[4])
print(l.index(1))
l.insert(2,"Hello")
print(l)
del l[4]
print(l)
l.remove('Hello')
print(l)