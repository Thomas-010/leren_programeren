pizzas = {
    "small": 6.50,
    "medium": 9.30,
    "large": 11.10
}

def vraag_aantal(maat):
    try:
        return int(input(f"Hoeveel {maat} pizza's wilt u?: "))
    except ValueError:
        print("Dit is geen heel nummer!")
        return 0

def print_kassabon(bestelling):
    totaal = 0
    print('**************Kassa bon**************')
    for maat, aantal in bestelling.items():
        if aantal > 0:
            prijs = pizzas[maat]
            subtotaal = prijs * aantal
            totaal += subtotaal
            print(f"Pizza's {maat}:\t  {aantal} x {prijs:.2f} = {subtotaal:.2f}")
    print('--------------------------------------')
    print(f'Te betalen:                   {totaal:.2f}')

def main():
    bestelling = {maat: vraag_aantal(maat) for maat in pizzas}
    print_kassabon(bestelling)


main()


