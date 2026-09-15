def vraag_gegevens():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    woonplaats = input("Wat is je woonplaats? ")
    
    gegevens = {
        "name": naam,
        "age": leeftijd,
        "city": woonplaats
    }

    volwassen = int(leeftijd) >= 18
    gegevens["is_volwassen"] = volwassen
    
    return gegevens


def verzamel_gegevens():
    personen = []

    while True:
        persoon = vraag_gegevens()
        personen.append(persoon)

        doorgaan = input("Toets enter om door te gaan of stop om te printen: ")

        if doorgaan == "stop":
            break

    return personen
