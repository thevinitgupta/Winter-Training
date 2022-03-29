import ctypes

class MyList:
    def __init__(self) -> None:
        self.size = 1 #current capacity of list
        self.n = 0 #current no. of items in list
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        #*using the ctype module to make an array of C type with size capacity and returns it
        return (capacity*ctypes.py_object)