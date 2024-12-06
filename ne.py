def calculator():
    try:
        num1 = float(input("First number"))
        num2 = float(input("Your second number"))
        operation = input("Enter the operation (+, -, *, /): ")


        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2}= {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2}= {result}")

        elif operation == "*":
            result = num1 * num2
            print(f"{num1} *{num2}= {result}")
        elif operation == "/":
            if num2 !=0:
                result = num1 / num2
                print(f"{num1} / {num2}= {result}")

            else: 
                print("Infinity!")
        else:
            print("Please input a sign dumbass")
    except ValueError:
        print("Ghaii bratha")
            
calculator()
        
