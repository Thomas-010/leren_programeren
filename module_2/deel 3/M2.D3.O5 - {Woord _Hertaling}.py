vertaal_woorden = {
    "kat": "hond",
    "muur": "hek",
    "regen": "zonneschijn",
    "boek": "tablet",
    "stoel": "bank",
    "raam": "deur",
    "lamp": "fakkel"
}


def vertaal(tekst):
    woorden = tekst.split()
    nieuwwoord = []
    for woord in woorden:
        eerst = woord.strip(".,?!")
        if eerst in vertaal_woorden:
            nieuw = vertaal_woorden[eerst]
            nieuw += woord[len(eerst): ]
            nieuwwoord.append(nieuw)
        else:
            nieuwwoord.append(woord)
    return " ".join(nieuwwoord)

tekst = input ("Wat voor verhaaltje wil je vertalen:\n")
tekst = "kat muur regen boek, stoel raam lamp!"
    
output = vertaal(tekst)
print("\nVertaald")
print(output)



