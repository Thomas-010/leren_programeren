import functions

def vraag_getal(vraag_tekst):
    while True:
        try:
            return float(input(vraag_tekst))
        except ValueError:
            print('Fout: dit is geen geldige invoer')

print('Welkom bij de rekenmachine')
print('Welke bereking wilt u maken?')
print('A) Getallen optellen')
print('B) getallen aftrekken')
print('C) getallen vermenigvuldigen')
print('D) getallen delen')
print('E) getal ophogen')
print('F) getal verlagen')
print('G) getal verdubbelen')
print('H) getal halveren')

choice = input('Welke berekening wilt maken? (A, b, c, d, e, f ,g, h) ').lower()


eerste_keer = True

while True:
    if eerste_keer:
        n1 = vraag_getal('Geef het eerste getal: ')

    if choice in ('a', 'b', 'c', 'd'):
        n2 = vraag_getal('Geef het tweede getal: ')
    elif choice in ('e', 'f'):
        n2 = 1
    elif choice in ('g', 'h'):
        n2 = 2

    if choice in ('a', 'e'):
        resultaat = functions.addition(n1, n2)
        teken = '+'
    elif choice in ('b', "f"):
        resultaat = functions.subtraction(n1, n2)
        teken = '-'
    elif choice in ('c', 'g'):
        resultaat = functions.multiplication(n1, n2)
        teken = '*'
    elif choice in ('d', 'h'):
        resultaat = functions.division(n1, n2)
        teken = ':'

    print(n1, teken, n2, '=', resultaat)

    n1 = resultaat
    eerste_keer = False

    print(f'Wat wil je doen met de uitkomst {resultaat}?')
    print('A) Getallen optellen')
    print('B) getallen aftrekken')
    print('C) getallen vermenigvuldigen')
    print('D) getallen delen')
    print('E) getal ophogen')
    print('F) getal verlagen')
    print('G) getal verdubbelen')
    print('H) getal halveren')
    print('I) Niets')

    choice = input('Kies A, b, c, d, e, f ,g, h of i: ').lower()

    if choice == 'i':
        print('Rekenmachine sluit af. DOEI!')
        break
