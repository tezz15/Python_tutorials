a,  b = map(int,input().split(" "))
matrix = list()
for i in range(a):
    c = list()
    c = list((map(int,input().split(" "))))
    matrix.append(c)


for i in range(b):
    for j in range(a):
        print(matrix[j][i],end=" ")
    print()
