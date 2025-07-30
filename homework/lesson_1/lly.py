currentNumber = 0
previousNumber = 0
for currentNumber in range(0,10):
    sumNumber = previousNumber + currentNumber
    print('Current Number: ' + str(currentNumber) + ' Previous Number: ' + str(previousNumber) + ' sum: ' + str(sumNumber))
    currentNumber = currentNumber + 1
    previousNumber = currentNumber - 1