boodschappen = {}  

meer_toevoegen = True

while meer_toevoegen:

    if len(boodschappen) > 0:
        print(f"Je hebt momenteel {len(boodschappen)} artikel(en) op je lijstje.\n")
    
    artikel = input("Welk artikel wil je toevoegen aan je boodschappenlijstje? ")
    

    if artikel == "":
        print("Je hebt geen artikel ingevuld. Probeer opnieuw.\n")
        continue
    
    hoeveelheid = input(f"Hoeveel {artikel} wil je toevoegen? ")
    
    if hoeveelheid == "":
        print("Je hebt geen hoeveelheid ingevuld. Probeer opnieuw.\n")
        continue

    artikel_lowercase = artikel.lower()

    if artikel_lowercase in boodschappen:
        boodschappen[artikel_lowercase] = str(int(boodschappen[artikel_lowercase]) + int(hoeveelheid))
        print(f"De hoeveelheid van '{artikel}' is bijgewerkt!\n")
    else:
        boodschappen[artikel_lowercase] = hoeveelheid
        print(f"Je hebt {hoeveelheid} {artikel} toegevoegd aan je boodschappenlijstje.\n")
    

    antwoord = input("Wil je nog meer boodschappen toevoegen? (ja/nee): ")
    
    if antwoord != "ja":
        meer_toevoegen = False
    print()

print("JE BOODSCHAPPENLIJSTJE")
print("="*50)

if len(boodschappen) == 0:
    print("Je lijstje is leeg!")
else:
    for index, (artikel, hoeveelheid) in enumerate(boodschappen.items(), 1):
        print(f"{hoeveelheid}x {artikel}")
print("="*50)

