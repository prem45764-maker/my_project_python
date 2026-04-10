print("hello world")
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
op = input("enter a operator(+ , - , * , / , % , ** ) :")
if op == "+":
    print(num1 + num2) # obtain addition numbers
elif op ==  "-":
    print(num1 - num2)# obtain subtract number
elif op == "*":
    print(num1 * num2)# obtain multiply number
elif op == "%":
    print(num1 % num2)# obtain remainder number
elif op == "**":
    print(num1 ** num2)# obtain square number but num2 == 2 or obatin cube number but num2 == 3
elif op == "/":
    if num2 != 0:
        print(num1 / num2) # obtain divide number
    if num2 == 0:
        print("Error: division by zero")
else:
    print("error: invalid operator")
