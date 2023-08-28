class sample:
    x=23
    y=34
    @classmethod
    def ABC(cls):
        print(cls)
obj=sample()
obj.ABC()
sample.ABC()

def checkbal(self):
    print(f'available bal:{self.bal}')
@classmethod
def modifyROI(cls,x):
    cls.ROI=x
ob1=Bank('shashi',6896286,89429,8755)
ob1=Bank('vardhan',6896286,89429,8785)
ob1=Bank('telugu',6896286,89429,8745)

ob1.withdraw(555)
print(ob1.ROI)
Bank.modify(0.1)
print(ob1.ROI)
