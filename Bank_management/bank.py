# import random

# # Create Account
# accounts = {}

# class BankAccount:

#     def __init__(self, owner_name, balance = 0.00):
#         self.log("Created Bank Account!")
#         self.__account_number = self.generate_account_number()
#         self.__balance = balance
#         self.__owner_name = owner_name

#         # Add account
#         accounts[self.__owner_name] = self

#     def __str__(self):
#         return f"Name: {self.__owner_name}, Account Number: {self.__account_number}"
    
#     def generate_account_number(self):
#         account_number = random.randint(10000000, 99999999)
#         self.log(f"Your account number is  {account_number}")
#         return account_number

#     def getName(self):
#         self.log(f"Customer Name: {self.__owner_name}")
#         return self.__owner_name
    
#     def deposit(self, amount):
#         try:
#             if amount > 0:
#                 self.__balance += amount
#                 self.log(f"Payment Received for ${amount}")
#                 self.log(f"Payment Received for ${self.__balance}")
#                 return self.__balance
            
#             else:
#                 self.log("Deposit amount must be greater than 0")
#                 return "Inefficient amount to add"
#         except Exception as e:
#             self.log(e)
#             print(e)

#     def withdraw(self, amount):
#         try:
#             if amount <= self.__balance:
#                 self.__balance -= amount
#                 self.log(f"The amount of ${amount} has been deducted for your account")
#                 self.log(f"Available Balance is ${self.__balance}")
#                 return self.__balance
#             else:
#                 self.log("Your account balance is not enough to perform this transaction")
#                 return "Not enough founds"
#         except Exception as e:
#             print(e)

#     def getBalance(self):
#         self.log(f"You available balance is ${self.__balance}")
#         return self.__balance
    
#     def log(self, message):
#         with open("bankDetails.txt", "wt") as details:
#             data = details.write(message)
#             print(data, file="bankDetails.txt")

#     def displayAccountDetails(self):
#         self.log(f"Owner: {self.__owner_name}, Account Number: {self.__account_number}, Account Balance: {self.__balance}")





import random

# Global dictionary to store accounts by account number
accounts = {}

class BankAccount:
    def __init__(self, owner_name, balance=0.00):
        self.__account_number = self.generate_account_number()
        self.__balance = balance
        self.__owner_name = owner_name

        # Store the account in the global dictionary using account number as key
        accounts[self.__account_number] = self
        self.log(f"Created Bank Account for {self.__owner_name}!")

    def __str__(self):
        return f"Name: {self.__owner_name}, Account Number: {self.__account_number}"

    def generate_account_number(self):
        """Generate a random 8-digit account number."""
        account_number = random.randint(10000000, 99999999)
        self.log(f"Your account number is {account_number}")
        return account_number

    def get_owner_name(self):
        """Return the account owner's name."""
        self.log(f"Customer Name: {self.__owner_name}")
        return self.__owner_name

    def deposit(self, amount):
        """Deposit a valid amount into the account."""
        if amount > 0:
            self.__balance += amount
            self.log(f"Deposited ${amount:.2f}. New Balance: ${self.__balance:.2f}")
            return self.__balance
        else:
            self.log("Deposit amount must be greater than 0.")
            return "Invalid deposit amount."

    def withdraw(self, amount):
        """Withdraw a valid amount if sufficient balance exists."""
        if amount <= self.__balance:
            self.__balance -= amount
            self.log(f"Withdrew ${amount:.2f}. Remaining Balance: ${self.__balance:.2f}")
            return self.__balance
        else:
            self.log("Insufficient funds for this transaction.")
            return "Not enough funds."

    def get_balance(self):
        """Return the available balance."""
        self.log(f"Available Balance: ${self.__balance:.2f}")
        return self.__balance

    def log(self, message):
        """Log messages to a file."""
        with open("bankDetails.txt", "a") as details:
            details.write(f"{message}\n")
        print(f"[LOG]: {message}")

    def display_account_info(self):
        """Display the account details."""
        account_info = (f"Owner: {self.__owner_name}, "
                        f"Account Number: {self.__account_number}, "
                        f"Balance: ${self.__balance:.2f}")
        self.log(account_info)
        print(account_info)