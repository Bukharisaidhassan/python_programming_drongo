def reverse():
    num = 123456789
    reverse_number = 0
    print("Given number : ",num)
    while num > 0:
        # get the last number
        reminder = num % 10
        reverse_number = (reverse_number * 10) +  reminder
        # remove the last number
        num = num // 10
    print("Reverse number", reverse_number)    

        
    # return reverse_number

reverse()



