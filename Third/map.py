#Map function map()
'''
map() returns a list of the results after applying the given 
function to each item of a given iterable(list, tuple) etc.
syntax: map(fun, iterable)
'''
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)

print(arr[-1])  #Gives the largest value.
print(arr[-2])  #Gives the 2nd largest value. 
