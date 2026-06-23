def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
try:
    num1=float(input("Enter first number:"))
    num2=float(input("Enter the second number:"))

    print("\n Select Operation")
    print("1. Add")
    print("2.Substarct")
    print("3.Multipy")
    print("4.Divide")

    choice=input("Enter your choice(1-4):")
    if choice=="1":
        print("result:",add(num1,num2))
    elif choice=="2":
        print("result:",substract(num1,num2))
    elif choice=="3":
        print("result:",multiply(num1,num2))
    elif choice=="4":
        if num2==0:
            print("Cannot divide by zero")
        else:
            print("result",divide(num1,num2))
    else:
        print("Invalid Choice!")

except ValueError:
    print("Enter valid number")
    
