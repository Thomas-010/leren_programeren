def vraag_gegevens():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")


    gegevens = {
        "naam": naam,
        "leeftijd": leeftijd
    }

    return gegevens

persoon = vraag_gegevens()

print(f"{persoon['naam']} is {persoon['leeftijd']} jaar.")