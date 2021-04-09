#Nicole Peacock
#email: nap06c@gmail.com

from datetime import datetime
import random


# account has following format
# acountNumber: [firstName, lastName, email, password, balance]
accounts = {
    1234567890: ["Seyi", "Onifade", "xyluz@gmail.com", "seyi", 100.0],
    2345678901: ["Mike", "Evans", "mevans@gmail.com", "mike", 1000.0],
    3456789012: ["Love", "Jones", "ljones@yahoo.com", "love", 500.0]
}

#keep count of number of incorrect logins
incorrectLoginCount = 0


def init():
    print("\n\n######### Welcome to Bank XYZ #########\n")

    haveAccount = input("Do you already have an account with us? Enter yes or no \n")
    haveAccount = haveAccount.lower()

    if(haveAccount == "yes" or haveAccount == "y"):
        login()
    elif(haveAccount == "no" or haveAccount == "n"):
        register()
    else:
        print("You have entered an invalid response")
        init()

def login():
    print("\n\n######### Login #########\n")
    accountNumber = int(input("Please enter your account number\n"))
    password = input("Please enter your password\n")

    if(accountNumber in accounts):
        user_account = accounts[accountNumber]
        if(user_account[3] == password):
            dt = datetime.now()
            dt_time = dt.strftime("%H:%M:%S")
            dt_date = dt.strftime("%m/%d/%Y")
            print("\nWelcome %s %s. Logged in at %s on %s" % (user_account[0], user_account[1], dt_time, dt_date))
            bankMenu(user_account)
    print("You have entered an incorrect account number or password")

    # if user enters 3 or more incorrect passwords, take back to main menu
    global incorrectLoginCount
    incorrectLoginCount += 1
    if(incorrectLoginCount >= 3):
        incorrectLoginCount = 0
        print("User name and password have been entered incorrectly too many times. Returning to main screen")
        init()
    
    login()

def register():
    print("\n\n######### Registration #########\n")

    firstName = input("Enter your first name\n")
    lastName = input("Enter your last name\n")
    email = input("Enter your email address\n")
    balance = float(input("Enter your starting account balance\n"))
    password = input("Create a password\n")

    accountNumber = generateAccountNumber()
    accounts[accountNumber] = [firstName, lastName, email, password, balance]

    print("\nCongratulation %s %s, your account has been created." % (firstName, lastName))  
    print("Your account number is %d" % (accountNumber))

    login()

def generateAccountNumber():
    ranNum = random.randrange(1111111111,9999999999)

    # check if account number already exists
    if(ranNum in accounts):
        generateAccountNumber()
    
    return ranNum

def bankMenu(userAccount):
    print("\n\n######### Bank Main Menu #########\n")

    print("These are the available options:")
    print("(1) Withdrawal")
    print("(2) Cash Deposit")
    print("(3) Balance Inquiry")
    print("(4) Complaint")
    print("(5) Logout")
    print("(6) Exit")

    selectedOption = int(input("Please select an option: "))

    if(selectedOption == 1):
        withdrawal(userAccount)
    elif(selectedOption == 2):
        deposit(userAccount) 
    elif(selectedOption == 3):
        print("Your current balance is $%.2f" % userAccount[4])
    elif(selectedOption == 4):
        input("What issue would you like to report?\n")
        print("Thank you for contacting us")
    elif(selectedOption == 5):
        print("\nLogging out........")
        login()
    elif(selectedOption == 6):
        print("\nGoodbye")
        exit()
    else:
        print("You have selected an invalid option")

    bankMenu(userAccount)

            
def withdrawal(userAccount):
    withdrawAmount = float(input("How much would you like to withdraw\n"))
    if(withdrawAmount > userAccount[4]):
        print("Sorry, you do not have the required funds in your account to withdraw")
    else:
        userAccount[4] -= withdrawAmount
        print("Take your cash!")
        

def deposit(userAccount):
    depositAmt = float(input("How much would you like to deposit?\n"))
    userAccount[4] += depositAmt
    print("Your current balance is $%.2f" % userAccount[4])


init()


