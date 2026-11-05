pizzas = {
    "small": 6.50,
    "medium": 9.30,
    "large": 11.10
}

maten = list(pizzas)

def vraag_aantal(maat):
    while True:
        try:
            aantal = int(input(f"Hoeveel {maat} pizza's wilt u?: "))
            if aantal >= 0:
                return aantal
            print("Het aantal mag niet negatief zijn!")
        except ValueError:
            print("Dit is geen heel nummer!")

def print_regel(tekst, bedrag):
    print(f"{tekst}\t{bedrag:.2f}")


def print_pizzaregels(aantallen):
    totaal = 0
    for maat, aantal in zip(maten, aantallen):
            if aantal > 0:
                prijs = pizzas[maat]
                subtotaal = prijs * aantal
                totaal += subtotaal
                print(f"Pizza's {maat}:\t  {aantal} x {prijs:.2f} = {subtotaal:.2f}")
    return totaal

def print_kassabon(aantallen):
    print('**************Kassa bon**************')
    totaal = print_pizzaregels(aantallen)
    print('--------------------------------------')
    print(f'Te betalen:                   {totaal:.2f}')

def main():
    aantallen = [vraag_aantal(maat) for maat in maten] 
    print_kassabon(aantallen)


main()


