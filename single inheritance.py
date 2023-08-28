class Bankv1:
    Bname='SBI'
    Branch='Marathahalli'
    def __init__(self,Name,Acc,Mno,Bal):
        self.name=Name
        self.acc=Acc
        self.mno=Mno
        self.bal=Bal
class Bankv2(Bankv1):
    def __init__(self,Name,Acc,Mno,Bal,Pan,Email):
        super().__init__(Name,Acc,Mno,Bal)
        self.pan=Pan
        self.email=Email
obj=Bankv2('shashi',3435345,89898,50000,45647,'shashi@gmail.com')
print(obj.Bname)
print(obj.Branch)
print(obj.pan)
print(obj.acc)
print('\n')
#==========================================================================================================================================

class Bankv1:
    Bname='SBI'
    Branch='Marathahalli'
    def __init__(self,Name,Acc,Mno,Bal):
        self.name=Name
        self.acc=Acc
        self.mno=Mno
        self.bal=Bal
    def  details(self):
        print(f'Name:{self.name}')
        print(f'Acc:{self.acc}')
        print(f'Mno:{self.mno}')
        print(f'Bal:{self.bal}')
class Bankv2(Bankv1):
    def __init__(self,Name,Acc,Mno,Bal,Pan,Email):
        super().__init__(Name,Acc,Mno,Bal)
        self.pan=Pan
        self.email=Email
    def details(self):
        super().details()
        print(f'pan:{self.pan}')
        print(f'email:{self.email}')
obj=Bankv2('shashi',3435345,89898,50000,45647,'shashi@gmail.com')
'''print(obj.Bname)
print(obj.Branch)
print(obj.pan)
print(obj.acc)'''
obj.details()


