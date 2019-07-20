try:
    a = float(input("Enter 1st Number: "))
    op = input("Enter operator: ")
    b = float(input("Enter 2nd Number: "))
    #a op b = input("Enter number1 operator number2").split()
    if op == "+":
        print("Result is :" + str(a+b))

    elif op == "-":
        print("Result is: " + str(a-b))

    elif op == "*":
        print("Result is: " + str(a*b))

    elif op == "/":
        print("Result is: " + str(a/b))

    elif op == "%":
        print("Result is: " + str(a%b))
        
    else:
        print("Invalid Operator!")
except ValueError:
    print("You entered the wrong value.")


