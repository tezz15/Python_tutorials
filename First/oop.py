#Object Oriented Programming in python
class Computer():
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("Config is : ",self.cpu,self.ram)

com1 = Computer('Intel i3', 5)
com2 = Computer('Intel i5', 8)

com1.config()
com2.config()

     
