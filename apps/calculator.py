def run():
    print("Running calculator app...")
    print("app commands: add, sub, exit")
    while True:
        calculatorinput = input("> ")
        if calculatorinput == "exit":
            break
        if calculatorinput == "add":
             num1 = int(input("First Number >"))
             num2 = int(input("Second Number >"))
             numsum = num1 + num2
             print(numsum)
        if calculatorinput == "sub":
             num1 = int(input("First Number >"))
             num2 = int(input("Second Number >"))
             numsum = num1 - num2
             print(numsum)
    print("calculator app stopped.")