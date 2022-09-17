class employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole,alanguages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.language=alanguages

    def printdetails(self):
        return f"The Name is{self.name}.Salary is {self.salary} and role is {self.role}"
    @classmethod
    def chang_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("this is good"+string)
class Player:
    var=9
    no_of_game=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"The Name is {self.name}.Game is {self.game}"
class CoolProgramer(Player,Employee):
    language="C++"
    def printlanguage(self):
        print(self.language)


class Programmer(employee):
    def __init__(self,aname,asalary,arole,alanguages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.language=alanguages
    def printprog(self):
        return f"The Programmer Name is {self.name}.Salary is {self.salary} role is {self.role} and languages is {self.language}"


harry=employee("harry",266,"instructor","python")
rohan=employee("rohan",111,"student","python")
shubham=Programmer("Shubham",123,"Programmer","python")
karan=Programmer("Karan",777,"Programmer","python")
print(karan.printprog())