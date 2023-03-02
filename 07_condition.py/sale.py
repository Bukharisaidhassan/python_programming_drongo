def sale():
    item1 = int(input("Price of computer sale : "))
    item2 = int(input("Price of laptob sale : "))
    amount = item1 + item2
    print("Total amount of two items : ", amount)

    if (amount > 0):
        if amount <= 25000:
            disc = amount * 0.02
        elif amount <= 15000:
            disc = amount * 0.03
        elif amount <= 10000:
            disc = amount * 0.04
        else:
            disc = amount * 0.03

    print("Discount : ", disc)
    print("Net pay : ", amount - disc)


sale()
