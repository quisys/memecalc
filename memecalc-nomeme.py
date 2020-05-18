import os
clear = lambda: os.system('clear')

clear()
while True:
    while True:
        op= (input("op "))
        if op not in ["add","sub","mul","div"]:
            print("please enter add, sub, mul or div")
        else:
            break
    while True:
        try:
            n1= int(input("n1 "))
        except ValueError:
            print("please enter a number")
        else:
            if op == "div":
                if n1 == 0:
                    print("can't divide by 0")
                else:
                    break
            else:
                break
    while True:
        try:
            n2= int(input("n2 "))
        except ValueError:
            print("please enter a number")
        else:
            if op == "div":
                if n2 == 0:
                    print("can't divide by 0")
                else:
                    break
            else:
                break
    if op == "add":
        p= n1+n2
    if op == "sub":
        p = n1-n2
    if op == "mul":
        p = n1*n2
    if op == "div": 
        p = n1/n2
    print(p)
    again= (input("again? [y/n] "))
    if again == "y":
        clear()
    if again == "n":
        clear()
        print("goodbye")
        break
