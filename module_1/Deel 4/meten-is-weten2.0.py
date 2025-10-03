nr1 = int(input('Wat is het 1ste getal?:'))
nr2 = int(input('Wat is het 2de getal?:'))

minimum = min(nr1, nr2)
maximum = max(nr1, nr2)

verschil = abs(nr1 - nr2)

nr1 = int(nr1)
nr2 = int(nr2)


if nr1 == nr2:
    print (f'Beide getallen zijn even groot (nr1: {nr1}, nr2: {nr2})')
elif nr1 > nr2:
    print (f'nr1 ({nr1}) is groter dan nr2 ({nr2})')
else:
    print (f'nr2 ({nr2}) is groter dan nr1 ({nr1}))')

if verschil > 0:
    print (f'Het verschil tussen {nr1} en {nr2} is: {verschil}')

print (f'Het minimum is: {minimum} en het maximimum is: {maximum}')

