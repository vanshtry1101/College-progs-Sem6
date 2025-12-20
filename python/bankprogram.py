class bank(object):
    cash=10000000
    @classmethod
    def available_cash(cls):
        print(cls.cash)

class andhrabank(bank):
    pass

class statebank(bank):
    cash=20000000
    @classmethod
    def available_cash(cls):
        print(cls.cash+bank.cash)

a=andhrabank()
a.available_cash()

s=statebank()
s.available_cash()
