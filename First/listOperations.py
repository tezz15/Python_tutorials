a = [1,2,3,4]
b = [5,6,7,8]
#print(a+b)
#print(a*3)
sum = list()
sub = list()
mul = list()
div = list()

for i in range(0,len(a)):
    sum.append(a[i]+b[i])
    sub.append(a[i]-b[i])
    mul.append(a[i]*b[i])
    div.append(a[i]/b[i])
print("The list of sum is: ", sum)
print("The list of sub is: ", sub)
print("The list of mul is: ", mul)
print("The list of div is: ", div)