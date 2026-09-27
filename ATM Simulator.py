#ATM Simulator
Balance=10000
PIN=1234

def Check_balance():
    print("The existing balance is:",Balance)

def Deposit():
    global Balance
    User=int(input("Enter the amount to be depositted:"))
    Balance+=User
    print("The amount is depositted successfully!")
    print("The current balance is:",Balance)

def Withdraw():
    global Balance
    User=int(input("Enter the amount to be withdrawn:"))
    if Balance>=User:
        Balance-=User
        print("The amount is withdrawn successfully!")
        print("The current balance is:",Balance)
    else:
        print("Insufficient balance!")

ch="yes"

ATM_Pin=int(input("Enter the 4-digit pin number:"))
if ATM_Pin==PIN:
    while ch.lower() in ["yes","y"]:
        print("---ATM MENU---")
        print("1.Check the balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        choice=int(input("Enter the choice number:"))
        if choice==1:
            Check_balance()
        elif choice==2:
            Deposit()
        elif choice==3:
            Withdraw()
        elif choice==4:
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice entered")
        ch=input("Do you want to continue(yes/no)?")
else:
    print("Incorrect PIN entered!")
   
