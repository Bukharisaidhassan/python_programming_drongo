

def get_discount():
    item1 = int(input("Enter sale item : "))

    item2 = int(input("Enter sale item : "))

    amout = item1 + item2


    if (amout > 0):
        if (amout <= 10000):
            disc = amout * 0.02
        elif amout <= 15000:
            disc = amout * 0.03
        elif amout <= 20000:
            disc = amout * 0.04

        else:
            disc = 0.05 * amout
        print("Discount : ", disc)
        print("Net pay : ", amout - disc)

get_discount()