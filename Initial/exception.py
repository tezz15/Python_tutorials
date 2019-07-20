#try and except
#What is the use of try and exception? 
try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a/b)

except ZeroDivisionError:
    print("Division by Zero! ")

except ValueError:
    print(ValueError)
