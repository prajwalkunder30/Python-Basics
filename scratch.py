class employee:
    no_of_leaves=90
    def __init__(self,aname,arole,asalary):
        self.name=aname
        self.role=arole
        self.salary=asalary
    def printdetails(self):
        return f"The Name is {self.name},salary is {self.salary} and role is {self.role}"
    def __add__(self,other):
        return self.name + other.name

emp1=employee("prajwal",450,"Instructor")
emp2=employee("kajal",300,"Dancer")
print(emp1+emp2)
