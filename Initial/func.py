a = "NEPAL"

#print(a)
#print(a[::-1]) #To reverse the string.

#print(a[::-2])
for i in range(1,len(a)+1):
    print(i)
    print(a[0:i])
print('\n')
for i in range(1,len(a)+1):
    print(a[:i])
#    print(i)
print('\n')
print(a[5::-1])
print('\n')
#print(a[0:5])
#for i in range(0,len(a)):
#    print(a[i:0:-1])

for i in range(len(a)-1,-1,-1):
    print(i)
    print(a[i::-1])
