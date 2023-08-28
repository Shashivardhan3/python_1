class Bank:
    bankname = 'SBI'
    branchname = 'marathahalli'
    roi = 0.08

    def __init__(self, name, accno, mno, bal, pin):
        self.name = name
        self.accno = accno
        self.mno = mno
        self.bal = bal
        self.pin = pin

    def deposit(self, amt):
        if self.pin == self.getpin():
            self.bal += amt
            print('Deposited successfully')
        else:
            print('Invalid pin')

    def withdraw(self, amt):
        if self.pin == self.getpin():
            if self.bal >= amt:
                self.bal -= amt
                print('Amount withdrawn successfully')
            else:
                print('Insufficient funds')
        else:
            print('Invalid pin')

    @staticmethod
    def getpin():
        x = int(input('Enter pin: '))
        return x

    def checkbal(self):
        if self.pin == self.getpin():
            print(f'Available balance: {self.bal}')
        else:
            print('Invalid pin')

    @classmethod
    def modifyroi(cls, x):
        cls.roi = x


ob1 = Bank('shashi', 7846742836, 785998734, 9879, 5645645)
ob2 = Bank('vardhan', 7846742836, 785998734, 9879, 5645645)
ob3 = Bank('telugu', 7846742836, 785998734, 9879, 5645645)
ob2.checkbal()
ob2.withdraw(1000)
ob2.checkbal()
