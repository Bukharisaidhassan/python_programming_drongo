num = 756325
count = 0
while num != 0:
    num = num // 10
    print(f"Number is {num}")
    count = count + 1 
    print(f"count is {count}")
    print("\n\n")
print("Total digits are : ",count)    