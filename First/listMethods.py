#append, extend, sort
#for deleting: del, pop, remove

a = [6,2,1,3,4,5,'a','b']

#append method appends the parameter to the list.
a.append('c')
print(a)
print('\n')

b = ['m','n','p','u','q','o','t','s']
#extend method extends the list.
a.extend(b)     #this doesnot change the value of list b. Here, a is extended. 
print(a)
print('\n')

#sort method sorts the value of list.
#a.sort() 
b.sort()
print(b)

print('\n')
#DELETING ELEMENTS
#pop and del are used when you know the index of the value of the list which is to be deleted.
#remove is used when you do not know the index but the value that is to be deleted.

a.pop(1) #deletes the value 2. Since it has index 1. 
print(a)

print('\n')
del b[1] #deletes the value 
print(b)

print('\n')
b.remove('t')
print(b)