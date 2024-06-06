class Bank:
    def __init__(self):
        self.clients = {}
        self.admins = {}
        self.t_balance = 0
        self.t_loan = 0
        self.loan_enable = True