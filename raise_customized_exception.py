# How to define and raise customize exception

class VoteException(Exception):
    def __init__(self,argv):
        self.msg = argv

age = int(input('enter the age :'))
try :
    if age < 18:
        raise VoteException('This is not valid age')
    else :
        print('You are eligible for voting')
except VoteException as msg :
    print(msg)
