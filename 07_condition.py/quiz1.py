def items():

    cost1 = int(input("Enter a cost expencive of item1 : "))
    cost2 = int(input("Enter a cost cheap of item2 : "))

    if (cost1 > cost2):
        disc = cost2 * 0.5
        print(disc)
        total = disc + cost1
        print(total)

    else:
        total = cost1 + cost2
        print(total)
        print(disc)
        

items()

 



