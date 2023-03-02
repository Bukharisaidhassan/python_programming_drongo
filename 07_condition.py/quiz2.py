

def get_discount():
    item1 = int(input("Enter sale item : "))

    item2 = int(input("Enter sale item : "))

    amount = item1 + item2
    print("Total amount of two items is : ", amount)

    if (amount > 0):
        if (amount <= 10000):
            disc = amount * 0.02
        elif amount <= 15000:
            disc = amount * 0.03
        elif amount <= 20000:
            disc = amount * 0.04

        else:
            disc = 0.05 * amount
        print("Discount : ", disc)
        print("Net pay : ", amount - disc)

get_discount()
















































