'''
a = [1,2,3,4]
b = [3,4,7,6]
c = list()
d = list()
for i in range(0,len(a)):
    c.append(a[i]+b[i])
    d.append(a[i]**b[i])
print(c)
print(d)
'''
a = [4,5,6,9]
a.append(7)
print(a)
b = [2,3,8,6]
a.extend(b)
print(a)

a.sort()
print(a)
