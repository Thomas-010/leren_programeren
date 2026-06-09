import random

namen_lijst = []

while True:
    naam = input("Voer een naam in: ").strip()

    if naam in namen_lijst:
        print("Deze naam is al ingevoerd. Probeer een andere naam.")
        continue

    namen_lijst.append(naam)

    if len(namen_lijst) < 3:
        continue


    keuze = input("Wil je nog een naam toevoegen of wil je lootjes trekken? (toevoegen/trekken)").strip().lower()

    if keuze == "toevoegen":
        continue
    elif keuze == "trekken":
        break
    else:
        print ("Ongeldige keuze, probeer opnieuw.")
        namen_lijst.pop() 


while True:
    lootjes = namen_lijst[:]
    random.shuffle(lootjes)

    if all(namen_lijst[i] != lootjes[i] for i in range(len(namen_lijst))):
        break 

print("\n --- Lootjes zijn getrokken! ---")
print("Voer je naam in om te zien wie je hebt")


while True: 
    naam = input("\n Voer je naam in of 'stop' om af te sluiten:")

    if naam.lower() == "stop":
        print("Tot de volgende keer!") 
        break

    if naam in namen_lijst:
        index = namen_lijst.index(naam)
        print(f"Jij hebt: {lootjes[index]}")
    else:
        print("Deze naam is niet bekend!")