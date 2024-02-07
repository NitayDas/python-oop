class Student:
    def __init__(self,name,dept):
        self.name = name 
        self.dept = dept
        
    def ShowDetails(self):
        print(f"Name : {self.name}")
        print(f"Department : {self.dept}\n")
        
    def comparing(self,student):
        if self.dept == student.dept:
            print(f"They are from dept of :{self.dept}\n")
        else:
            print(f"They are not from same dept\n")
            
            
student1 = Student("Nitay", "CSE")
student2 = Student("Rafi", "CSE")
student3 = Student("Anik", "BME")

student1.ShowDetails()
student2.ShowDetails()
student3.ShowDetails()

student1.comparing(student2)
student1.comparing(student3)


        