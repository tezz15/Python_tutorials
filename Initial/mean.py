n = 5
x = [1,5,5,7,6]
sum = 0
a=len(x)
b = int(a/2)

for index in range(a):
    sum+= x[index]

print("Mean")
mean = (sum / n)
print(mean)

median = (x[b-1] + x[b])/2
print("Median")
print(median)

y = x.sort()
count = 0
for index in range(a):
    elif x[0]==x[index]:
        count = count + 1
        c = count
    elif x[1]==x[index]:
        count = count + 1
        d = count
    elif x[2]==x[index]:
        count = count + 1
        e = count
    elif x[3]==x[index]:
        count = count + 1
        e = count
    elif x[4]==x[index]:
        count = count + 1
        f = count
if c >= d and c>= e and c>=f:
    print(x[0])

if d >= c and d>=e and d>=f:
    print(x[1])

if 


