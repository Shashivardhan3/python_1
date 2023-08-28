class bankv1:
    Bname = 'SBI'
    Branch = 'Maratahalli'
    def __init__(self, name, acc, mno, bal):
        self.name = name
        self.acc = acc
        self.mno = mno
        self.bal = bal
    def details(self):
        print(f'name:{self.name}')
        print(f'acc:{self.acc}')
        print(f'mno:{self.mno}')
        print(f'bal:{self.bal}')

class bankv2(bankv1):
    def __init__(self, name, acc, mno, bal, pan, email):
        super().__init__(name, acc, mno, bal)
        self.pan = pan
        self.email = email
    def details(self):
        super().details()
        print(f'pan:{self.pan}')
        print(f'email:{self.email}')
        

class bankv3(bankv2):
    def __init__(self, name, acc, mno, bal, pan, email, aadhar):
        super().__init__(name, acc, mno, bal, pan, email)
        self.aadhar = aadhar
    def details(self):
        super().details()
        print(f'aadhar:{self.aadhar}')

obj = bankv3('shashi', 3435345, 89898, 50000, 45647, 'shashi@gmail.com', 4363656)
print(obj.Bname)
print(obj.name)
obj.details()
