class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.clients = {}
        self.admins = {}
        self.t_balance = 0
        self.t_loan = 0
        self.loan_enable = True

    def create_account(self, user_type, user_name, primary_deposit=0):
        if user_type == 'user':
            if user_name not in self.clients:
                self.clients[user_name] = User(user_name, primary_deposit)
                self.t_balance += primary_deposit
                print(f"Welcome to {self.bank_name} as a new client")
            else:
                print(f"{user_name} already exists")
        elif user_type == 'admin':
            if user_name not in self.admins:
                self.admins[user_name] = Admin(user_name)
                print(f"Account has been created for {user_name} as Admin")
            else:
                print(f"{user_name} already exists as Admin")
        else:
            print("Invalid user type")

    def get_total_balance(self):
        return self.t_balance
    
    def get_total_loan(self):
        return self.t_loan
    
    def loan_feature_toggle(self, status):
        self.loan_enable = status
        print(f"Loan is now {'enabled' if status else 'disabled'}")


class User:
    def __init__(self, user_name, balance=0):
        self.user_name = user_name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"{amount} deposited successfully")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrew {amount} successfully")
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance
    
    def transfer_amount(self, amount, receiver_username, bank):
        if amount <= self.balance:
            if receiver_username in bank.clients:
                self.balance -= amount
                bank.clients[receiver_username].balance += amount
                self.transaction_history.append(f"Transferred {amount} to {receiver_username}")
                bank.clients[receiver_username].transaction_history.append(f"Received: {amount} from {self.user_name}")
                print(f"{amount} transferred to {receiver_username} successfully")
            else:
                print("Receiver does not exist.")
        else:
            print("Insufficient funds")

    def check_history(self):
        return self.transaction_history
    
    def take_loan(self, bank):
        if bank.loan_enable:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            bank.t_loan += loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
            print(f"Loan of {loan_amount} granted successfully.")
        else:
            print("Loan feature is currently disabled.")


class Admin:
    def __init__(self, user_name):
        self.username = user_name

    def check_total_balance(self, bank):
        return bank.get_total_balance()

    def check_total_loans(self, bank):
        return bank.get_total_loan()

    def toggle_loan_feature(self, bank, status):
        bank.loan_feature_toggle(status)


def user_menu(user, bank):
    while True:
        print("\nUser Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer Amount")
        print("5. Check Transaction History")
        print("6. Take Loan")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif choice == '3':
            print(f"Available balance: {user.check_balance()}")
        elif choice == '4':
            amount = float(input("Enter amount to transfer: "))
            receiver_username = input("Enter receiver's username: ")
            user.transfer_amount(amount, receiver_username, bank)
        elif choice == '5':
            print("Transaction History:")
            for transaction in user.check_history():
                print(transaction)
        elif choice == '6':
            user.take_loan(bank)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")


def admin_menu(admin, bank):
    while True:
        print("\nAdmin Menu")
        print("1. Check Total Balance")
        print("2. Check Total Loans")
        print("3. Toggle Loan Feature")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print(f"Total balance of the bank: {admin.check_total_balance(bank)}")
        elif choice == '2':
            print(f"Total loan amount: {admin.check_total_loans(bank)}")
        elif choice == '3':
            status = input("Enter 'True' to enable loan feature or 'False' to disable: ").lower() == 'true'
            admin.toggle_loan_feature(bank, status)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")


# Main Program
bank = Bank("Bank Asia")

# Admin Create Account
bank.create_account('admin', "admin1")

# User Create Accounts
bank.create_account('user', "Monir", 5000)
bank.create_account('user', "Runa", 10000)

# Access User and Admin Menus
Monir = bank.clients["Monir"]
Runa = bank.clients["Runa"]
admin1 = bank.admins["admin1"]

# User Menu for Monir
user_menu(Monir, bank)

# User Menu for Runa
user_menu(Runa, bank)

# Admin Menu for admin1
admin_menu(admin1, bank)