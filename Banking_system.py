account={}

def transfer(user):
    if len(account)<2:
        print("NOT ENOUGH USERS TO TRANSFER!")
    else:
        receiver=input("ENTER THE RECEIVER'S USERNAME: ").strip().upper()

        if receiver not in account:
            print(receiver,"DOES NOT EXIST!")

        elif receiver==user:
            print("YOU CANNOT TRANSFER MONEY TO YOURSELF!")
            return

        else:
            try:
                cost=int(input("ENTER THE AMOUNT: "))

                if cost>account[user]["BALANCE"]:
                    print("INSUFFICIENT FUNDS!")

                elif cost<=0:
                    print("INVALID AMOUNT!")

                else:
                    account[user]["BALANCE"]-=cost
                    account[receiver]["BALANCE"]+=cost

                    print(f"Rs.{cost} TRANSFERRED SUCCESSFULLY!")

                    account[user]["HISTORY"].append(
                        f"Rs.{cost} TRANSFERRED TO {receiver} | BALANCE:{account[user]['BALANCE']}"
                    )

                    account[receiver]["HISTORY"].append(
                        f"Rs.{cost} RECEIVED FROM {user} | BALANCE:{account[receiver]['BALANCE']}"
                    )

            except ValueError:
                print("INVALID INPUT!")


def history(user):
    print("TRANSACTION HISTORY:")

    if not account[user]["HISTORY"]:
        print("NO TRANSACTIONS FOUND!")

    else:
        for t in account[user]["HISTORY"]:
            print(t)


def deposit(user):
    while True:
        try:
            amount=int(input("ENTER THE AMOUNT: "))

            if amount<=0:
                print("INVALID AMOUNT!")

            else:
                account[user]["BALANCE"]+=amount

                print(f"Rs.{amount} DEPOSITED!!")

                account[user]["HISTORY"].append(
                    f"Rs.{amount} DEPOSITED | BALANCE:{account[user]['BALANCE']}"
                )

                break

        except ValueError:
            print("INVALID INPUT!")


def withdraw(user):
    while True:
        try:
            money=int(input("ENTER THE AMOUNT: "))

            if money>account[user]["BALANCE"]:
                print("INSUFFICIENT FUNDS!")

            elif money<=0:
                print("INVALID AMOUNT!")

            else:
                account[user]["BALANCE"]-=money

                print(f"Rs.{money} WITHDRAWN!!")

                account[user]["HISTORY"].append(
                    f"Rs.{money} WITHDRAWN | BALANCE:{account[user]['BALANCE']}"
                )

                break

        except ValueError:
            print("INVALID INPUT!")


def display(user):
    print("CURRENT BALANCE:", account[user]["BALANCE"])


def change(user):
    old=input("ENTER PIN: ")

    if old==account[user]["PIN"]:

        new=input("SET PIN: ")

        if len(new)!=4 or not new.isdigit():
            print("INVALID PIN!")

        else:
            account[user]["PIN"]=new

            print("PIN RESET!")

            account[user]["HISTORY"].append("PIN CHANGED")

    else:
        print("WRONG PIN!")


def create(account):
    username=input("ENTER USERNAME: ").strip().upper()

    if username in account:
        print("USERNAME ALREADY EXISTS!")
        return

    pin=input("SET PIN: ")

    if len(pin)!=4 or not pin.isdigit():
        print("INVALID PIN!")

    else:
        try:
            balance=int(input("ENTER YOUR BALANCE: "))

            if balance<0:
                print("INVALID AMOUNT!")
                return

            account[username]={
                "PIN":pin,
                "BALANCE":balance,
                "HISTORY":[]
            }

            print("ACCOUNT CREATED SUCCESSFULLY!")

            account[username]["HISTORY"].append(
                f"ACCOUNT CREATED | BALANCE:{account[username]['BALANCE']}"
            )

        except ValueError:
            print("INVALID INPUT!")


def login(account):
    user=input("ENTER USERNAME: ").strip().upper()

    if user in account:

        for i in range(3):

            password=input("ENTER PIN: ")

            if password==account[user]["PIN"]:

                print("LOGIN SUCCESSFUL!!")

                account[user]["HISTORY"].append("LOGGED IN")

                break

            else:
                print(f"WRONG PIN! ATTEMPTS LEFT:{2-i}")

        else:
            print("TOO MANY WRONG ATTEMPTS!")
            return

        while True:

            print("-"*40,"MENU","-"*40)
            print("1.DEPOSIT")
            print("2.WITHDRAW")
            print("3.DISPLAY")
            print("4.CHANGE PIN")
            print("5.TRANSACTION HISTORY")
            print("6.TRANSFER MONEY")
            print("7.LOG OUT")

            choose=input("ENTER: ")

            if choose=="1":
                deposit(user)

            elif choose=="2":
                withdraw(user)

            elif choose=="3":
                display(user)

            elif choose=="4":
                change(user)

            elif choose=="5":
                history(user)

            elif choose=="6":
                transfer(user)

            elif choose=="7":

                print("THANK YOU FOR USING OUR BANKING SYSTEM!!")

                account[user]["HISTORY"].append("LOGGED OUT")

                break

            else:
                print("INVALID OPTION!")

    else:
        print(user,"DOES NOT EXIST!")


while True:

    print("\n1.CREATE ACCOUNT")
    print("2.LOGIN")
    print("3.EXIT")

    choice=input("ENTER: ")

    if choice=="1":
        create(account)

    elif choice=="2":
        login(account)

    elif choice=="3":
        print("GOODBYE!")
        break

    else:
        print("INVALID OPTION!")
        
