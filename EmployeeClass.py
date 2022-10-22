class Employee:
    def __init__(self,name,a,g,s,desig,depart):
         self.name=name
         self.age=a
         self.gender=g
         self.salary=s
         self.designation=desig
         self.department=depart
    def display(self):
         print("Name- ",self.name)
         print("Age- ",self.age)  
         print("Gender- ",self.gender)   
         print("Salary- ",self.salary)   
         print("Designation- ",self.designation)   
         print("Department- ",self.department)

e1=Employee("harry",20,"M",1000,"md","research")
e1.display()            
            
         