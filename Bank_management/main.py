from bank import BankAccount, accounts

def create_account():
    owner_name = input("Enter the account owner's name: ").capitalize()
    account = BankAccount(owner_name)
    print("\nAccount successfully created!")
    account.display_account_info()

def check_balance():
    try:
        account_number = int(input("Enter the account number: "))
        account = accounts.get(account_number)
        if account:
            print(f"Account Balance for {account.get_owner_name()}: ${account.get_balance():.2f}")
        else:
            print("Account not found. Please check the account number.")
    except ValueError:
        print("Invalid input. Please enter a valid account number.")

def deposit_amount():
    try:
        account_number = int(input("Enter the account number: "))
        account = accounts.get(account_number)
        if account:
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount > 0:
                    account.deposit(amount)
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        else:
            print("Account not found. Please check the account number.")
    except ValueError:
        print("Invalid input. Please enter a valid account number.")

def main():
    while True:
        print("\n--- Bank Account Management ---")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Amount")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            check_balance()
        elif choice == '3':
            deposit_amount()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
