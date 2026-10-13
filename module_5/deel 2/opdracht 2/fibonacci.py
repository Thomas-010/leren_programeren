def vraag_aantal(prompt:str) -> int:
    while True:
        try:
            aantal = int(input(prompt))
            if aantal >= 2:
                return aantal
            print('Minimum is 2')
        except:
            print('Voer een geldig heel getal in!')

def bereken_fibonacci(positie: int) -> int:
    nummer = 0
    volgend_getal = 1
    for i in range(positie):
        nieuw_getal = nummer + volgend_getal
        nummer = volgend_getal
        volgend_getal = nieuw_getal
    return nummer

def bereken_gulden_snede(nummer: int, volgend_getal: int) -> float:
    return nummer / volgend_getal

def maak_reeks_tekst(aantal: int) -> str:
    tekst = str(bereken_fibonacci(0))
    for postitie in range(1, aantal):
        tekst = tekst + ',' + str(bereken_fibonacci(postitie))
    return tekst  


aantal = vraag_aantal('Hoeveel getallen uit de reeks wil je zien?  ')
print(maak_reeks_tekst(aantal))

voorlaatste = bereken_fibonacci(aantal - 2)
laatste = bereken_fibonacci(aantal - 1)
gulden_snede = bereken_gulden_snede(voorlaatste, laatste)
print(f'Guldlen snede is: {voorlaatste} / {laatste} = {gulden_snede:.6f}')
