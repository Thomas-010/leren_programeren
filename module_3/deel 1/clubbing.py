PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de flowchart na

bandje = "Je krijgt van mij een {kleur} bandje"
stempel = "Je krijgt van mij een stempel"
geentoegang = "Sorry je mag niet naar binnen"
compliment = "Alstublieft, complimenten van het huis"
probeerjaarlater = "Probeer het in een {hvljaar} jaar nog eens"
geenideegw = "Sorry geen idee wat je bedoeld, hier een glasje water"
geenalcohol = "Sorry je mag geen alcohol bestellen onder de 21"
champagne = "Sorry alleen vips mogen champagne bestellen"
betalen = "Asjeblieft je {drank}, dat is dan {prijs}"

PRIJZEN = {
    "cola": PRIJS_COLA,
    "bier": PRIJS_BIER,
    "champagne": PRIJS_CHAMPAGNE
}

leeftijd = int(input('Hoe oud ben je?'))

if leeftijd < 18:
    print(geentoegang)
    hvljaar = 18 - leeftijd
    print(probeerjaarlater.format(hvljaar=hvljaar))
    quit()

naam = input("Wat is je naam? ")
heeft_bandje = False
heeft_stempel = False
kleur = None

if naam in VIP_LIST:
    heeft_bandje = True
    if leeftijd >= 21:
        kleur = "blauw"
    else:
        kleur = "rood"
    print(bandje.format(kleur=kleur))
else:
    if leeftijd >= 21:
        heeft_stempel = True
        print(stempel)

print("Wat wil je drinken?")
drank = input("Cola, bier of champagne? ").lower()

if drank not in DRANKJES:
    print(geenideegw)

elif drank == "cola":
    if heeft_bandje:
        print(compliment)
    else:
        prijs = PRIJZEN[drank]
        print(betalen.format(drank=drank, prijs=f"{prijs:.2f}"))

elif drank == "bier":
    if leeftijd < 21:
        print(geenalcohol)
    elif heeft_bandje and heeft_stempel:
        print(compliment)
    else:
        prijs = PRIJZEN[drank]
        print(betalen.format(drank=drank, prijs=f"{prijs:.2f}"))

elif drank == "champagne":
    if not heeft_bandje:
        print(champagne)
    elif kleur != "blauw":
        print(geenalcohol)
    else:
        prijs = PRIJZEN[drank]
        print(betalen.format(drank=drank, prijs=f"{prijs:.2f}"))

print("Einde programma")
