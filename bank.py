import sqlite3
import random as rand
class Bank:
    print("WELCOME TO DB BANK")
    print("-------------------")
    def __init__(self):
        self.file = sqlite3.connect("Bank.db")
        self.c = self.file.cursor()

    def CreateAccount(self):       
        self.c.execute("""create table if not exists Customer
            (
                User_Name text,
                Account_Number integer,
                Account_Balance integer,
                Deposit integer,
                Withdraw integer,
                Transfer integer
            )""")
        n1 = input("Enter your First Name:- ").upper()
        n2 = input("Enter Your Last Name:- ").upper()
        print("---------------------------------------")
        if n1.isalpha() and not n1.isspace() and n2.isalpha() and not n2.isspace() and len(n1)>2 and len(n2)>2:
            name = n1+" "+n2
            number = rand.randint(10000000,99999999)
            self.balance = 0
            self.deposit_amount = 0
            self.Withdraw_amount = 0
            self.Transfer_amount = 0
            self.c.execute("insert into Customer values(?,?,?,?,?,?)",(name,number,self.balance, self.deposit_amount, self.Withdraw_amount, self.Transfer_amount ))
            print("Hello {} your Account was successfully created. Please note your Account Number.".format(name))
            print("Your Account Number is:- {}".format(number))
            print("---------------------------------------")
            self.file.commit()
            self.file.close()
            #self.c.execute("select * from Customer")
            #print(self.c.fetchall())
            
        else:
            print("Enter Valid Name, Try Again...!")


            
    def Login(self):
        acc_no = int(input("Enter your Account Number:- "))
        check = True
        flag = False
        for a,b,c,d,e,f in self.c.execute("select * from Customer"):
            if b == acc_no:
                flag = True
                check = False
                total = c
                identity = a
                # amt_dp = d
                # amt_wt = e
                # amt_trans = f
                print("(C)-Check Balance")
                print("(D)-Deposit")
                print("(W)-Withdraw")
                print("(T)-Transfer")
                print("(E)-Exit")
                option = input("What would you like to do today? (C)/(D)/(W)/(T)")
            
        if flag and (option=='d' or option=='D'):
            amt_dp = int(input("Enter the amount to Deposit:- "))
            deposit = amt_dp + total 
            self.c.execute("update Customer set Account_Balance = ?, Deposit = ? where Account_Number = ?",(deposit,amt_dp,acc_no))
            self.file.commit()
            print("amount Deposited ${} , Available Balance is ${} ".format(amt_dp,deposit))
            # self.c.execute("select * from Customer")
            # print(self.c.fetchall())

        if flag and (option == 'w' or option == 'W'): 
            amt_wt = int(input("Enter the amount to Withdraw:- "))
            if total>0 and total >= amt_wt:
                withdraw_bal = total - amt_wt
                self.c.execute("update Customer set Account_Balance = ?, Withdraw = ? where Account_Number = ?",(withdraw_bal, amt_wt,acc_no))
                self.file.commit()
                print("Withdraw ${} done successfully...! Available balance ${}".format(amt_wt,withdraw_bal))
                # self.c.execute("select * from Customer")
                # print(self.c.fetchall())

            else:
                print("Low Balance")

        if flag and (option == 't' or option == 'T'): 
            amt_trans = int(input("Enter the amount to Transfer:- "))
            if total>0 and total >= amt_trans:
                transfer_amt = total - amt_trans
                self.c.execute("update Customer set Account_Balance = ?, Transfer = ? where Account_Number = ?",(transfer_amt,amt_trans,acc_no))
                self.file.commit()
                print("Transfer ${} done successfully...! Available balance ${}".format(amt_trans,transfer_amt))
                # self.c.execute("select * from Customer")
                # print(self.c.fetchall())

        if flag and (option == 'c' or option == 'C'):
            print("Hello {}, Your Account Balance is ${}".format(identity,total))
        print("----------------------------------------------------------")
        if check:
            print("Invalid Account Number.")

        if flag and (option == 'e' or option == 'E'):
            bk = Bank;

fun = Bank()
print("(C)-Create Account")
print("(O)-Open Account")
op = input("What would you like to do today? (C)/(O):- ")
if op == 'c' or op == 'C':
 fun.CreateAccount()
if op =='o' or op == 'O':
 fun.Login()