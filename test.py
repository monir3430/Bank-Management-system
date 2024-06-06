class Bank:
    def __init__(self):
        self.customers = {}
        self.admins = {}
        self.total_balance = 0
        self.total_loans = 0
        self.loan_feature_enabled = True

    def create_account(self, user_type, username, initial_deposit=0):
        if user_type == 'user':
            if username not in self.customers:
                self.customers[username] = User(username, initial_deposit)
                self.total_balance += initial_deposit
                print(f"Account created for user '{username}' with initial deposit of {initial_deposit}")
            else:
                print("User account already exists.")
        elif user_type == 'admin':
            if username not in self.admins:
                self.admins[username] = Admin(username)
                print(f"Account created for admin '{username}'")
            else:
                print("Admin account already exists.")
        else:
            print("Invalid user type.")

    def get_total_balance(self):
        return self.total_balance

    def get_total_loans(self):
        return self.total_loans

    def toggle_loan_feature(self, status):
        self.loan_feature_enabled = status
        print(f"Loan feature is now {'enabled' if status else 'disabled'}")

class User:
    def __init__(self, username, balance=0):
        self.username = username
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        return self.balance

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            if recipient in bank.customers:
                self.balance -= amount
                bank.customers[recipient].balance += amount
                self.transaction_history.append(f"Transferred: {amount} to {recipient}")
                bank.customers[recipient].transaction_history.append(f"Received: {amount} from {self.username}")
                print(f"{amount} transferred to {recipient} successfully.")
            else:
                print("Recipient does not exist.")
        else:
            print("Insufficient funds.")

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, bank):
        if bank.loan_feature_enabled:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            bank.total_loans += loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
            print(f"Loan of {loan_amount} granted successfully.")
        else:
            print("Loan feature is currently disabled.")

class Admin:
    def __init__(self, username):
        self.username = username

    def check_total_balance(self, bank):
        return bank.get_total_balance()

    def check_total_loans(self, bank):
        return bank.get_total_loans()

    def toggle_loan_feature(self, bank, status):
        bank.toggle_loan_feature(status)

# Creating bank instance
bank = Bank()

# Admin creating user accounts
bank.create_account('user', 'alice', 1000)
bank.create_account('user', 'bob', 500)

# User operations
alice = bank.customers['alice']
bob = bank.customers['bob']

alice.deposit(500)
alice.withdraw(200)
print(alice.check_balance())

alice.transfer(300, 'bob')
print(bob.check_balance())

alice.take_loan(bank)
print(alice.check_balance())
print(bank.get_total_loans())

# Checking transaction history
print(alice.check_transaction_history())
print(bob.check_transaction_history())

# Admin operations
bank.create_account('admin', 'admin1')
admin1 = bank.admins['admin1']

print(admin1.check_total_balance(bank))
print(admin1.check_total_loans(bank))

admin1.toggle_loan_feature(bank, False)
alice.take_loan(bank)  # Should print that loan feature is disabled
