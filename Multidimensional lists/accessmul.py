#Accessing multidimensional lists with the help of loop
a = [[1,2,3],[4,5,6],[9,8,7]]
for i in a:
    print(i)

#Accessing multidimensional lists using square brackets or index
b = [[2,4,5],[3,5,6],[9,8,7]]

for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=" ")
    print()

#Creating multidimensional list with the help of user input.
row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

matrix = list()

print("Enter the entries rowwise: ")
for r in range(row):
    a = list()
    for c in range(column):
        a.append(int(input()))
    matrix.append(a)

print(matrix)



