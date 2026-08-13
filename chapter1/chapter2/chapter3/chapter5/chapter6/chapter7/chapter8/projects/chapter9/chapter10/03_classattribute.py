class Employee:
    name = "sinchana"
    age = 20
    centre = "Delhi"
    
    def printobj(self):
        print(f"The name is {self.name}")
    
    @staticmethod
    def greet():
        print("good day")   
    
    
details = Employee() # abasic object
detail = Employee() 
print(details.name)
print(detail.name)
detail.name ="monisha"
print(detail.name)
print(details.age)
print(details.centre)
details.printobj()
Employee.greet()