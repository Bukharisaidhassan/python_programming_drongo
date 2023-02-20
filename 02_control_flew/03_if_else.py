time = int(input("Enter a number : "))
if time == 9:
    print("On time")

elif time > 9 and time <= 12:
    print("10 minutes late")
elif time > 12 and time <= 15:
    print("30 minutes late")

else:
    print("Zero marks")
            