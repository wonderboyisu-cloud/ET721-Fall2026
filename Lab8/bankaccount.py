class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal!")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")

        self.balance -= amount

    def get_balance(self):
        return self.balance

# Local test
"""
    test = BankAccount("Bugs", 1000)
    print(f"\n{test.owner} has amount = ${test.balance}") # 1000
    test.deposit(500)
    print(f"After 500 deposit, amount = ${test.balance}") # 1500
    test.withdraw(100)
    print(f"After 100 withdraw, amount = ${test.balance}") # 1400
    test.withdraw(1400)
    print(f"After 1400 withdraw, amount = ${test.balance}") # 0
    test.deposit(1000)
    print(f"After 1000 deposit, amount = ${test.balance}") # 1000

    print(f"Final Balance = ${test.get_balance()}")
"""