import random
import sys


class BankApplication:
    bankName = 'crazyBank'

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.createAccount()

    def createAccount(self):
        print('Account created for user:', self.name)
        print('Bank Name               :', BankApplication.bankName)
        print('Account number          :', random.random())
        print('Account Balance         :', self.balance)
        print('*' * 30)

    def depositAmount(self, amount):
        self.balance = self.balance + amount
        print(
            '{} you have deposited Rs.{} in your account .Avaliable balance is {}'.format(self.name, amount,
                                                                                          self.balance))

    def withdrawAmt(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print(
                '{} you have withdrawn Rs.{} from your account .Avaliable balance is {}'.format(self.name, amount,
                                                                                                self.balance))
        else:
            print('Insufficient balance in your account')
            sys.exit()


name = input("Enter a name :")
ba = BankApplication(name)
print('Your account has been created successfully')
print('-------------------------------------------')
while True:
    print('What do you wish to do \n 1.Withdraw \n 2.deposit \n 3.Exit ')
    option = int(input('Choose an option :'))
    if option == 1:
        amt = int(input('Enter amount to be withdraw:'))
        ba.withdrawAmt(amt)
        print('********Thank you for withdrawing from {}*********'.format(BankApplication.bankName))

    elif option == 2:
        amt = int(input('Enter amount to be deposited:'))
        ba.depositAmount(amt)
        print('********Thank you for depositing in {}*********** '.format(BankApplication.bankName))

    else:
        print('Invalid option entered .Thank you!!!')
        sys.exit()
