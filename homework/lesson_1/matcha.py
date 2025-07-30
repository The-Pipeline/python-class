while True:
    print ('Printing current and previous number sum in a range')
    i = input ('Input desired number of iterations >')
    x = 0 #Current Number
    y = 0 #Previous Number
    while int(i) >= int(x): #Flow control
        print(' Current Number ' + str(int(x)) + ' Previous Number ' + str(int(y)) + ' Sum: ' + str(int(x) + int(y)))
        y = int(x)
        x = int(x)+1