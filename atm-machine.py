import time

print("PLEASE INSERT YOUR CARD")
time.sleep(5)
password=3043

pin = int(input("enter your pin"))
balance=5000

if pin == password:
    while True:

        print("""
            1 == BALANCE
            2 == WITHDRAW BALANCE
            3 == DIPOSIT BALANCE
            4 == EXIT
            """
            )
        try:
            option=int(input("PLEASE ENTER YOUR CHOISE"))
        except:
            print("PLEASE ENTER VALID OPTION")

        if option==1:
            print(f"YOUR CURRENT BALANCE IS {balance}")

        if option==2:
            
            withdraw_amount=int(input("PLEASE ENTER WITHDRAW AMOUNT"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your current balance is {balance}")

        if option==3:
            
            deposit_amount=int(input("PLEASE ENTER deposit AMOUNT"))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited from your account")
            print(f"your updated balance is {balance}")

        if option==4:
            break

else:
    print("YOU ENTER WRONG PASSWORD, TRY AGAIN")