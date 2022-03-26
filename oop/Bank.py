# 什么是class，什么是Object

class BankAccount:

    # Constructor 构造器
    def __init__(self, acccountNumber, accountName, balance):

        # 下面这几个是成员变量 instance variable 指的是针对每一个银行账号都有自己的这些变量
        self.accountNumber = acccountNumber
        self.accountName = accountName
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        pass

    def withdraw(self, amount):
        self.balance = self.balance - amount
        pass

    # 修改内置方法，以什么方式呈现出来（print类的时候）
    def __str__(self):
        return f'({self.accountName}, {self.balance})'

    # 比较自己的balance和别人的balance
    def __lt__(self, other):
        return self.balance < other.balance

