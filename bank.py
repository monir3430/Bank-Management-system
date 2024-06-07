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

# Bank Name & Instance
bank = Bank("Bank Asia")

# Admin Create Account
bank.create_account('user', "Monir", 5000)
bank.create_account('user', "Runa", 10000)

# User Activities
Monir = bank.clients["Monir"]
Runa = bank.clients["Runa"]

Monir.deposit(3000)
Monir.withdraw(2000)
print(f"Monir's Balance: {Monir.check_balance()}")

Monir.transfer_amount(250, 'Runa', bank)
print(f"Runa's Balance: {Runa.check_balance()}")

Monir.take_loan(bank)
print(Monir.check_balance())
print(bank.get_total_loan())


# Checking transaction history
print(Monir.check_history())
print(Runa.check_history())


# Admin Activities
bank.create_account('admin', 'admin1')
admin1 = bank.admins['admin1']

print(admin1.check_total_balance(bank))
print(admin1.check_total_loans(bank))

admin1.toggle_loan_feature(bank, False)
Monir.take_loan(bank)  # Should print that loan feature is disabled

admin1.toggle_loan_feature(bank, True)
Runa.take_loan(bank)  # Should print that loan feature is Enabled