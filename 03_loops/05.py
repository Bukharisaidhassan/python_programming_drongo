
def arithmetic():
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter second number : "))

    add = number1 + number2
    sub = number1 - number2
    mod = number1 % number2
    div = number1 / number2
    mult = number1 * number2

    print(f"Result (add {add})\n (sub{sub})\n {mod}\n{div}\n{mult}")


arithmetic()
