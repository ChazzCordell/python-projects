class BankAccount:
  accounts = []
  def __init__(self, int_rate, balance):
    self.int_rate = int_rate
    self.balance = balance
    BankAccount.accounts.append(self)
      # your code here! (remember, instance attributes go here)
      # don't worry about user info here; we'll involve the User class soon

  def deposit(self, amount):
    self.balance += amount
    return self
      # your code here

  def withdraw(self, amount):
    if(self.balance - amount) >=0:
      self.balance -= amount
    else:
      print("Insufficient funds: Charging a $5 fee")
      self.balance -= 5
      return self
      # your code here

  def display_account_info(self):
    print(f"Balance: {self.balance}")
    return self

  def yield_interest(self):
    if self.balance > 0:
        self.balance += (self.balance * self.int_rate)
    return self

  @classmethod
  def print_all_accounts(cls):
    for account in cls.accounts:
      account.display_account_info()

savings = BankAccount(.05, 1000)
checking = BankAccount(.02,5000)

savings.deposit(10).deposit(20).deposit(40).withdraw(100).yield_interest().display_account_info()
checking.deposit(10).deposit(20).deposit(40).withdraw(100).yield_interest().display_account_info()

BankAccount.print_all_accounts()
