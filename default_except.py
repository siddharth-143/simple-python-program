# default exception block

try :
    a = int(input('Enter 1st number :'))
    b = int(input('enter 2nd number :'))
    c = a/b
    print('Division :',c)

except ZeroDivisionError as msg :
    print('Exception handle',msg)

except :
    print('Default except')
