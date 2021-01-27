# Exception Handling with many exception

try :
    print(x)
    
except NameError :
    print('Variable x is not defined')

except :
    print('something else went wrong')


# Print one message if the try block raises a 'NameError' and another for other error
