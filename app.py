class mini_bank:
    '''This is a demo bank application developed by shiva'''

    # Class variable for bank name
    bank_name = "RBSN Bank"

    def __init__(self, name, balance=0.000):
        '''Initialize a customer with name and optional initial balance'''
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        '''Method to deposit money into the account'''
        confirm = input("Are you sure to perform this action: [Y/N]: ")
        if confirm.lower() == "y":
            self.balance = self.balance + amount
            print("After Deposit: ", self.balance)

    def withdraw(self, amount):
        '''Method to withdraw money from the account'''
        if amount > self.balance:
            print("Insufficient balance")
        else:
            confirm = input("Are you sure to perform this action: [Y/N]: ")
            if confirm.lower() == "y":
                self.balance = self.balance - amount
                print("After withdraw: ", self.balance)

    def check(self):
        '''Method to check the current balance'''
        print("Your current balance", self.balance)

# Display welcome message with the bank name
print("Welcome to", mini_bank.bank_name)

# Get customer's name as input
name = input("Enter your name: ")

# Create an instance of mini_bank for the customer
c = mini_bank(name)

# Greet the customer
print("Welcome", c.name)

# Main menu loop
while True:
    print('''\n
          P to set the HSP(High Security Pin)
          D to deposit
          W to withdraw
          C to balance check
          E to exit
          ''')

    # Get user's choice of action
    option = input("Choose an option: ")

    # Execute the selected option
    if option.lower() == 'd':
        amount = float(input("Enter an amount: "))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input("Enter an amount: "))
        c.withdraw(amount)
    elif option.lower() == 'c':
        c.check()
    elif option.lower() == 'e':
        print("Thank You", c.name, 'For Choosing', c.bank_name)
        break
    else:
        print("Please choose a valid option")
