import random
computer = random.choice([1,-1,0])
youstr = input("enter the value:")
youdict={"r":1,"p":-1,"s":0}
reversedict= {1:"r",-1:"p",0:"s"}
you= youdict[youstr]
print(f"you choose:{reversedict[you]}\ncomputer choose:{reversedict[computer]}")
if (computer==you):
    print("its draw")
else:
    if (computer==1 and you==0):
        print("computer wins")
    elif(computer==0 and you==1):
        print("you win!!")
    if (computer==-1 and you==0):
        print("you wins")
    elif(computer==0 and you==-1):
        print("computer win!!")
    elif(computer==-1 and you==1):
        print("computer win!!")
    elif(computer==1 and you==-1):
        print("you win!!")
    else:
        print("something went wrong")
