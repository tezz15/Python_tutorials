a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = float(input("Enter another number: "))

if a>b and a>c:
    print(a , " is the largest number.")

elif b>a and b>c:
    print(b , " is the largest number.")

else:
    print("%.2f is the largest number."%c)