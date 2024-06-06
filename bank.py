class Bank:
    
    def __init__(self, bank_name):
        self.Bank_name = bank_name
        self.clients = {}
        self.admins = {}
        self.t_balance = 0
        self.t_loan = 0
        self.loan_enable = True

    def create_account(self, user_type,user_name, primary_deposit=0):
        if user_type =='user':
            if user_name not in self.clients:
                self.clients[user_name] = User(user_name, primary_deposit)
                self.t_balance += primary_deposit
                print(f"Welcome to {self.Bank_name} as a new client")

            else:
                print(f"{user_name} already existed")

        else:
            print("Invalid user type")










class User:
    def __init__(self, user_name, balance = 0):
        self.user_name = user_name
        self.balance = balance
        self.transaction_history = []