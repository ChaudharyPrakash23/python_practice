x=int(input("enter the value of X :"))

match x:
    case 0:
        print(" x is zero")
    case 1:
        print("x is 1")
    case _ if x!=6:
        print(" x is not 6")
    case _:
        print(" x is not here")