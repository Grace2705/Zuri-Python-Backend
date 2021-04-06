## Import necessary Modules
from datetime import datetime
import random

## The user database
userdict = {'Praise':['Praise', 'babs', 'pb@gmail.com', 1267100234, 'pwdPrais'],
                'Grace':['Grace','umoren','gu@gmail.com', 3390598267,'pwdGrace'], 
                'Femi':['Femi','okedeyi','fo@gmailcom', 2390501235, 'pwdFemi'],
                'Yusuf':['Yusuf','opoola','yo@gmail.com', 6909285005, 'pwdYusuf']}


## Initailize the System
def init():
    daydate = datetime.now()
    print(daydate.strftime("%B %d %Y %H:%M:%S %p"))
    print('----------------------------------')
    print('Welcome to our bank\n')
    haveaccount = int(input('Do you have an account with us?\n 1(Yes) \n 2(No)\n'))
    if haveaccount == 1:
        login()
    elif haveaccount == 2:
        register()
    else:
        print('Invalid Option, Please try again')
        init()
    
## Allow user login
def login():
    #login function here
    name = input("Input your username? \n")
    password = input("Enter your password\n")
    if(name in userdict and password == userdict[name][-1]):
        print('#########')
        print('Login Successful...')
        print("Welcome " + name)
        bankOperations()
    else:
        print("Password or Username Incorrect. Please try again")
        login()
        
## Allow new users register
def register():
    print('REGISTER HERE')
    email = input('Enter your email address: ')
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    username = input('Enter your user name: ')
    password = input('Enter your password: ')
    accountno = generateaccountno()

    userdict[username] = [firstname, lastname, email, accountno, password]
    print('**********************')
    print('Your account has been created successfully')
    print('********')
    print('Your account number is: ', accountno)
    login()


## Generates account number for new users
def generateaccountno():
    return random.randrange(1000000000, 9999999999)


## Allow registered users carry out operations
def bankOperations():
    
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    Option = int(input('Please select an option:'))
                
    if(Option == 1):
        print('You selected option %s' % Option)
        withdraw = input('How much would you like to withdraw: ')
        print('...PROCESSING...')
        print('Please take your cash')
        Option2 = int(input('Do you want to perform another operation?\n 1(Yes) \n 2(No)\n'))
        if Option2 == 1:
            bankOperations()
        else:
            logout()
     
    elif(Option == 2):
        print('You selected option %s' % Option)
        deposit = input('How much would you like to deposit: ')
        print('You deposited: ', deposit)
        Option2 = int(input('Do you want to perform another operation?\n 1(Yes) \n 2(No)\n'))
        if Option2 == 1:
            bankOperations()
        else:
            goodbyemessage()
                    
    elif(Option == 3):
        print('You selected option %s' % Option)
        report = input('What issue will you like to report?')
        print('Thank you for contacting us')
        Option2 = int(input('Do you want to perform another operation?\n 1(Yes) \n 2(No)\n'))
        if Option2 == 1:
            bankOperations()
        else:
            goodbyemessage()
                    
    else:
        print('Invalid Option selected, please try again')
        bankOperations()

def goodbyemessage():
    print('Thank you for using our bank')
    logout()

def logout():
    exit()

init()