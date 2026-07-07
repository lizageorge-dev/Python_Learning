# Arithemetic operations using input function
Number1=input("Enter first number: ")
Number2=input("Enter second number: ")
operation=input("Enter the operation you want to perform (+, -, *, /): ")
if(Number1.isdigit() and Number2.isdigit() and operation in ['+', '-', '*', '/']):
 print("The result is: ", eval(Number1 + operation + Number2))
else:
 print("Invalid input. Please enter valid numbers and operation.")