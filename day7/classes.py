#classes

class Employee():
#function inside a class is called a method
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.fullname = fname + " " + lname

admin = Employee("David","Akuma")
finance = Employee("Frank", "John")


print(admin.fullname)
print(finance.fullname)