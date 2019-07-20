n = int(input())
arr = list()
#for i in range(n):
#    arr = list(map(int,input().split("\n")))

#for i in range(n):
#    print(arr[-(i+1)])

for i in range(n):
    arr.append(int(input()))

for i in range(n):
    print(arr[-(i+1)])