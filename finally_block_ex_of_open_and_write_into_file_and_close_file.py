# Try to open and write to a file that is not writtable

try :
    f = open('demofile.txt')
    f.write('wel-come to exception handling')

except :
    print('Something went wrong when writting to file')

finally :
    f.close()

# The program can continue, without leaving the file object open
