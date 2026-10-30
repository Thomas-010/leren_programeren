import random

namen_lijst = []
verlanglijst = {}

while True:
    naam = input("Voer een naam in: ").strip().lower()

    if naam == "":
        print("Vul een geldige naam in")
        continue

    if naam in namen_lijst:
        print("Deze naam is al ingevoerd. Probeer een andere naam.")
        continue

    cadeaus = []
    print(f'Welke 3 cadeautjes zou {naam} willen krijgen?: ')
    while len(cadeaus) < 3:
        cadeau = input(f'Cadeau {len(cadeaus) + 1}: ').strip()
        if cadeau == "":
            print("Vul een geldig cadeau in")
            continue
        cadeaus.append(cadeau)


    namen_lijst.append(naam)
    verlanglijst[naam] = cadeaus

    if len(namen_lijst) < 3:
        continue

    while True:
        keuze = input("Wil je nog een naam toevoegen of wil je lootjes trekken? (toevoegen/trekken): ").strip().lower()
        if keuze in ("toevoegen", "trekken"):
            break
        print("Ongeldige keuze. Kies 'toevoegen' of 'trekken'.")

    if keuze == "trekken":
        break

while True:
    lootjes = namen_lijst[:]
    random.shuffle(lootjes)

    if all(namen_lijst[i] != lootjes[i] for i in range(len(namen_lijst))):
        break 

print("\n --- Lootjes zijn getrokken! ---")
print("Voer je naam in om te zien wie je hebt")


while True: 
    naam = input("\n Voer je naam in of 'stop' om af te sluiten:").strip().lower()

    if naam.lower() == "stop":
        print("Tot de volgende keer!") 
        break

    if naam in namen_lijst:
        index = namen_lijst.index(naam)
        getrokken = lootjes[index]
        print(f"Jij hebt: {getrokken}")
        print(f"Dit staat op het lootje van {getrokken}:")
        for nummer, cadeau in enumerate(verlanglijst[getrokken], start=1):
            print(f' {nummer}. {cadeau}')
    else:
        print("Deze naam is niet bekend!")


print('\n --- Verlanglijstje ---')
for naam in namen_lijst:
    print(f'\n{naam}:')
    for nummer, cadeau in enumerate(verlanglijst[naam], start=1):
        print(f' {nummer}. {cadeau}')