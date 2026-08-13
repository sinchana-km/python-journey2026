class Employee:
    name = "sinchana"
    age = 20
    centre = "Delhi"
    
    def printobj(self):
        print(f"The name is {self.name}")
    
    
    
    
details = Employee() # a basic object 
print(details.name)
print(details.age)
print(details.centre)
details.printobj()