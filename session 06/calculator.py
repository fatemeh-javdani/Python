num1 = float(input("Enter the first number : "))
operation = input("Enter the operation")
num2 = float(input("Enter the second number : "))
if operation =="+":
    result = num1 + num2
    print(result)
elif operation =="-":
    result = num1 - num2
    print(result)
elif operation =="/":
    result = num1 / num2
    print(result)
elif operation =="*":
    result = num1 * num2
    print(result)
else:
    print("wrong input!")
    