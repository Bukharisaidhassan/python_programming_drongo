
amout = int(input("Enter sale item : "))

if (amout > 0):
    if (amout <= 10000):
        disc = amout * 0.2
    elif amout <= 15000:
        disc = amout * 0.3
    elif amout <= 20000:
        disc = amout * 0.4
       


      
    
    else:
        disc = 0.3 * amout
    print("Discount : ", disc)
    print("Net pay : ", amout)

