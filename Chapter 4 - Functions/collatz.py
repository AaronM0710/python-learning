import sys

def collatz(number):
    if number % 2 == 0:
        evenVar = number // 2
        print(evenVar, end = ' ')
        return evenVar
    else:
        oddVar = 3 * number + 1
        print(oddVar, end = ' ')
        return oddVar

try:
    number = int(input('Enter a number: '))
except ValueError:
    print('must enter an integer')
    sys.exit()

while number != 1:
    number = collatz(number)