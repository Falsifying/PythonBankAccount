import os
clear = lambda: os.system('cls')
clear()
CurrentMoney = 10
BankAccountMoney = 500

BankAccountname = input("Enter Your Name -- >")








def Starth() :
   clear()
   global CurrentMoney
   global BankAccountMoney
   converted_num = str(BankAccountMoney)

   print("Welcome - " + BankAccountname)
   print("Your Current Balance -- >$" + converted_num)

   converted_Money = str(CurrentMoney)
   print("Current Money --> $" + converted_Money)
   print("Deposit? Enter '1'")
   print("Withdraw? Press '2'")

   Decision = input("")
   

   converted_decision = int(Decision)

   if converted_decision == 1:
    clear()
    Amount = input("How much? -- ")
    convAmount = int(Amount)
    BankAccountMoney = convAmount + BankAccountMoney
    CurrentMoney = CurrentMoney - convAmount
    print("Thank you.")
    Starth()
 
   if converted_decision == 2:
    clear()
    Amount = input("How much? -- ")
    convAmount = int(Amount)
    BankAccountMoney = BankAccountMoney - convAmount
    CurrentMoney = CurrentMoney + convAmount
    print("Thank You.")
    Starth()

   else:
        clear()
        print("Incorrect Number, Please Try Again.")
        input("Press Enter to continue...")
        Starth()
   

   
    







Starth()


