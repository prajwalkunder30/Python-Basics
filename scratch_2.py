from abc import ABCMeta,abstractmethod
class shape:
    @abstractmethod
    def printarea(self):
         return 0
class Rectangle:
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=8
        self.breadth=9
    def printarea(self):
        return self.length*self.breadth
r=Rectangle()
print(r.length)