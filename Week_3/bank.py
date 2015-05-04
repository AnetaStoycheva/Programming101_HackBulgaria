class BankAccount:
    def __init__(self, name, balance, currency):
        self.__name = name
        self.__balance = balance
        self.__currency = currency
        self.__history = ['Account was created']

    def deposit(self, amount):
        self.__balance += amount
        self.__history.append('Deposited ' + str(amount) + str(self.__currency))

    def balance(self):
        self.__history.append('Balance check -> ' + str(self.__balance) + str(self.__currency))
        return self.__balance

    def withdraw(self, amount):
        if self.__balance < amount:
            self.__history.append('Unsuccessful withdraw of ' + str(amount) + str(self.__currency))
            return False
        else:
            self.__balance -= amount
            self.__history.append('Withdrawed ' + str(amount) + str(self.__currency))
            return True

    def __str__(self):
        return 'Bank account for {} with balance of {}{}'.\
            format(self.__name, self.__balance, self.__currency)

    def __int__(self):
        return self.__balance

    def transfer_to(self, other, amount):
        if self.__currency == other.__currency:
            if self.withdraw(amount):
                other.deposit(amount)
                self.__history.append('Transfer to ' + str(other.__name) + ' '\
                    + str(amount) + str(self.__currency))
                return True
        self.__history.append('Unsuccessful transfer to ' + str(other.__name)\
            + ' ' + str(amount) + str(self.__currency))
        return False

    def history(self):
        return self.__history
