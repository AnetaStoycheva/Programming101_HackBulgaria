class Bill:  # model na 1 banknota
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __int__(self):
        return self.amount

    def __str__(self):
        return "{}{}".format(self.amount, self.currency)
# ako tuk e "A {}{} bill." - dolu navsqkyde 6te print cqloto izr, a ne samo 10$

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __hash__(self):  # za da napravim re4nik ot banknoti
        return hash(self.__str__())


class BatchBill:
    def __init__(self, bills):
        self.bills = bills

    def __str__(self):
        return ', '.join([str(bill) for bill in self.bills])

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        return sum([int(bill) for bill in self.bills])


class CashDesk:

    def __init__(self):
        self.money_holder = {}

    def take_money(self, money):
        if isinstance(money, Bill):
            if money not in self.money_holder:
                self.money_holder[money] = 1
            else:
                self.money_holder[money] += 1
        else:
            for a_bill in money:
                if a_bill not in self.money_holder:
                    self.money_holder[a_bill] = 1
                else:
                    self.money_holder[a_bill] += 1

    def total(self):
        result = 0
        for key in self.money_holder:
            result += int(key) * self.money_holder[key]
        return result

    def inspect(self):
        for a_bill in self.money_holder:
            print('A bill of ' + str(a_bill) + ': ' + str(self.money_holder[a_bill]) + '.')


def main():
    a = Bill(10, "$")
    b = Bill(5, "$")
    c = Bill(10, "$")

    print(a.amount)  # 10
    print(a.currency)  # $
    print(int(a))  # 10
    print(str(a))  # '10 $' - taka bi trqbvalo da e
    print(a)  # 10$ --> eto tuk 6te printi "A 10 $ bill"
    print(b)  # 5$
    print(c)
    print(a == b)
    print(a == c)

    money_holder = {}
    money_holder[a] = 1  # We have one 10$ bill

    if c in money_holder:
        money_holder[c] += 1
    print(money_holder)  # {"A 10$ bill": 2}

    values = [10, 20, 50, 100]  # zip([10, 20, 50, 100], ['$', '$', '$', '$'])
    bills = [Bill(value, "$") for value in values]
    batch = BatchBill(bills)
    print(batch)
    for bill in batch:
        print(bill)

    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value, '$') for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10, '$'))

    print(desk.total())  # 390
    desk.inspect()

# A bill of 100$: 3.
# A bill of 10$: 2.
# A bill of 20$: 1.
# A bill of 50$: 1.


if __name__ == '__main__':
    main()
