class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance ${self.balance}"
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance ${self.balance}"
        else:
            return "Insufficient funds!"

    def transfer(self, amount, target_account):
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount

            return f"Transferred ${amount} to {target_account.account_holder}"
        else:
            return "Transfer failed: Insufficient funds!"


my_account = BankAccount("Ansh")
friend_account = BankAccount("Meet")

print(my_account.deposit(100))
print(my_account.transfer(40, friend_account))

print(f"Meet balance is now ${friend_account.balance}")




"""class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds!"

    def transfer(self, amount, target_account):
        # 1. Check if the sender (self) has enough money
        if amount <= self.balance:
            # 2. Remove money from the sender
            self.balance -= amount
            # 3. Add money to the receiver (target_account)
            target_account.balance += amount
            
            return f"Transferred ${amount} to {target_account.account_holder}."
        else:
            return "Transfer failed: Insufficient funds!"


# --- Testing our banking system ---

# Create two distinct accounts
my_account = BankAccount("Ansh")
friend_account = BankAccount("Sam")

# Put some money in your account
print(my_account.deposit(100))

# Transfer some of it to your friend
print(my_account.transfer(40, friend_account))

# Look directly at your friend's balance to prove the money arrived
print(f"Sam's balance is now: ${friend_account.balance}")"""