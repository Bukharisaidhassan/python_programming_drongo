def sumation():
    print("hello")
    user_name = input("Enter your name : ")

    print(user_name)
    print("Your name is"+user_name)

    phone_number = int(input("Enter phone number : "))
    print(phone_number)
    
    print(f"Your phone number is : {phone_number}")

    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    sum = num1 + num2
    print(f"sumation is {sum}")

if __name__ == '__main__':
    sumation()
