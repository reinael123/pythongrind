def simple_calculator():
    print("simple calculator")
    print("choose operation")
    print("1 add")
    print("2 sub")
    print("3 multiply")
    print("4 divide")


    operation = {
        1: ("add", lambda x, y : x + y),
        2: ("sub", lambda x, y : x - y),
        3: ("multiply", lambda x, y : x * y),
        4: ("divide", lambda x, y : x / y if y != 0 else "bobo di pwede yan")
    }


    while True:
        try:
            choice = int(input("enter operation: "))
            if choice not in operation:
                print("bobo mo talaga men, isa pa nga")
                continue
            break
        except ValueError:
                print("bobo mo naman")


    while True:
        try:
            num1 = float(input("enter first number: "))
            num2 = float(input("enter second number: "))
            break
        except ValueError:
            print("bobo mo naman")

    operation_name, operation_func = operation[choice]
    result = operation_func(num1, num2)

    if isinstance(result, str):
        print(result)
    else:
        print(f"the result of {operation_name} is {result} ")

    use_again = input("isa pa? y/n: ").lower().strip()
    if use_again == "y":
        simple_calculator()
    else:
        print("tapos na tayo tols")

if __name__ == "__main__":
    simple_calculator()
