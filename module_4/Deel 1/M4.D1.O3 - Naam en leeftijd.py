def vraag_gegevens():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    woontplaats = input("Wat is je woonplaats? ")


    gegevens = {
        "naam": naam,
        "leeftijd": leeftijd,
        "woontplaats": woontplaats
    }

    return gegevens

def verzamel_gegevens():
    personen = []

    while True:
        persoon = vraag_gegevens()
        personen.append(persoon)

        doorgaan = input("Toets enter om door te gaan of typ 'stop' om te stoppen: ")

        if doorgaan.lower() == 'stop':
            break

    return personen

personen = verzamel_gegevens()

for persoon in personen:
    print(f"{persoon['naam']}, die in {persoon['woontplaats']} woont, is {persoon['leeftijd']} jaar.")