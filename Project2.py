'''
calculator

'''
while True:
    a = int(input("Enter num1: "))
    operation = input("Choose operation:")
    b = int(input("Enter num2: "))
    match operation:
        case "+":
            print(a+b)
        case "-":
            print( a - b)
        case "*":
            print(a * b)
        case "/":
            print(a / b)
        case "%":
            print(a % b)
        case "**":
            print(a ** b)
        case _ :
            print("Something went wrong!")