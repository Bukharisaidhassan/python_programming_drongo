firstlist = [20]
secondlist = [20]

if firstlist == secondlist:
    print("lists are equal")
else:
    print("lists are NOT equal")

if firstlist is secondlist:
    print("both variables are pointing to the same object")
else:
    print("both variables are NOT pointing to the same object")

mylist1 = [10,20,30]
mylist2 = [40]
if mylist1[0] in mylist2:
    print("elements are overlapping")
else:
    print("elements are NOT overlapping")        

list = 90
mylist = [80,70,60,50]
if list is mylist:
    print("list is present")
else:
    print("list is NOT present")
