class Employee:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def printobj(self):
        print(f"The name is {self.name}")
        print(f"The marks is {self.marks}")
        
    
    
    
    
details = Employee("Harry",56) # a basic object 
detail = Employee("sinchana", 78)
details.printobj()
detail.printobj()
