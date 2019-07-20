a = [[1,2,3],[4,5,6]]
print(a[0]) #Prints all the elements of row 0. 
print(a[1]) #Prints all the elements of row 1. 
b = a[0]    #The list of row 0 is transferred to b. i.e. list b is created with the elements of a[0].
print(b)

print(a[0][1])  #Prints the specific value specified by the index. 

a[0][1] = 7     #New value is assigned in the specified list element.
print(a)
print(b)

b[2] = 9    #New value is assigned in the specified place. And b is one dimensional list.


