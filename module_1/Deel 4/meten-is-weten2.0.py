nr1 = input('Wat is het 1ste getal?:')
nr2 = input('Wat is het 2de getal?:')

minimum = 0
maximum = 1000

if nr1 == nr2:
    print (f'Beide getallen zijn even groot (nr1: {nr1}, nr2: {nr2})')
elif nr1 > nr2:
    print (f'nr1 ({nr1}) is groter dan nr2 ({nr2})')
else:
    print (f'nr2 ({nr2}) is groter dan nr1 ({nr1}))')


print (f'Het minimum is: {minimum} en het maximimum is: {maximum}')
