"""t=int(input())
for execution in range(1,t+1):
    num1=int(input("Enter a number:"))
    num2=int(input("Enter second number:"))
    operator=input("Enter a operator(+,-,*,**,/,%,//):")
    if (operator== "+")
        print(num1+num2)
    elif (operator == "-"):
        print(num1-num2)
    elif (operator == "*"):
        print(num1*num2)
    elif (operator == "**"):
        print(num1**num2)
    elif (operator == "/"):
        print(num1/num2)
    elif (operator == "%"):
        print(num1%num2)
    elif (operator == "//"):
        print(num1//num2)
    else:
        print("Enter a valid integer or number")"""

def calculator(num1,num2):
    operator=input("Enter a operator(+,*,-,/,//,%):")
    if operator =="+" :
        return num1+num2
num1=int(input())
num2=int(input())
print(calculator(num1,num2))
    
