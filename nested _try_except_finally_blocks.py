# Nestest try except finally blocks

try :
    print('Outer try block')
    try :
        print('Inner try block')
        print(10/2)
    except ZeroDivisionError :
        print('Inner except block')
    finally :
        print('Inner finslly block')

except :
    print('Outer except block')
finally :
    print('Outer finslly block')
