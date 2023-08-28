class Bank:
    bankname:'sbi'
    nob=10000
    def __init__(self,name,acc,mno,bal):
        self.name=name
        
        self.acc=acc
        self.mno=mno
        self.bal=bal

    def details(self):
        print(f'name :{self.name}')
        print(f'acc :{self.acc}')
        print(f'mno:{self.mno}')
        print(f'bal:{self.bal}')
obj1=Bank('shashi',759585,7685637,987589897)
obj2=Bank('vardhan',756875,7868687,99709709)
ob1.details()
