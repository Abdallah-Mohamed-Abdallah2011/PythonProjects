print("Welcome to Simple calculator, give me your problem")

def addtion(x, y):
    return(x + y)

def subtraction(x, y):
    return (x - y)

def multiplication(x, y):
    return(x * y)

def division(x, y):

    if y == 0:

        return ("Error")

    return (x / y)

def calculator():

    print("simple calculator")

print("1. Adding (+)")

print("2. subtracing (-)")

print("3. multipling (*)")

print("4. dividing (/)")



opr = input("select your operation :")

num1 = float(input("Enter your first Number  :"))

num2 = float(input("Enter your second Number  :"))



if opr in ['1', '2', '3', '4']:
    if opr == '1':
       result = addtion(num1, num2)
    elif opr == '2':
        result = subtraction(num1, num2)
    elif opr =='3':
        result = multiplication(num1, num2)
    elif opr == '4':
        result = division(num1, num2)
    print("Your result is   :", result)             

     
print("thanks you for using my calculator")
