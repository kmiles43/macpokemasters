from B import B
from A import A
from C import C
from D import D


def mainPoke():
    ans1 = "B"
    # ans1 = input("What would you like to do: "
    #              " A.Find out if you could catch a pokemon"
    #              " B.See how many badges you could obtain with your current party"
    #              " C.Simulate a one vs one battle"
    #              " D. What Move should you use")
    if ans1 == "A" or ans1 == "a":
        A()
    elif ans1 == "B" or ans1 =="b":
       B()

    elif ans1 == "C" or ans1 =="c":
        C()
    elif ans1 == "d" or ans1 == "D":
        D()
    else:
        print("Wrong input")



mainPoke()