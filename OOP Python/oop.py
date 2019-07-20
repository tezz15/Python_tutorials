class Computer:
    def brand(self,name,ram):
        self.name = name
        self.ram = ram
        print(self.name)
        print(self.ram)
class House(Computer):
    def size(self,size):
        self.size = size
        print(self.size)
'''
str = Computer()
str1 = Computer()
str.brand('dell','32gb')
str1.brand('lenovo','16gb')
'''
h1 = House()
h1.size(12)
h1.brand('acer','8')