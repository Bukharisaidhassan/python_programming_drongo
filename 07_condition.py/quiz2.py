
amout = int(input("Enter sale item : "))

if (amout > 0):
    if (amout <= 10000):
        disc = amout * 0.02
    elif amout <= 15000:
        disc = amout * 0.03
    elif amout <= 20000:
        disc = amout * 0.04

    else:
        disc = 0.3 * amout
    print("Discount : ", disc)
    print("Net pay : ", amout)
