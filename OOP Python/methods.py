class Student:
    
    school = 'Lumbini Engineering College'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3 

    def avg(self):          #This is instance method.  
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def get_school(cls):          #class method
        return cls.school
    
    @staticmethod
    def info():
        print("This is static method.")

s1 = Student(43,55,88)
s2 = Student(65,48,98)

print(s1.avg())    
print(s2.avg())
print(Student.get_school())           #calling class method. 

Student.info()                          #calling static method
