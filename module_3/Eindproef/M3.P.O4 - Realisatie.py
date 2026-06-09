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

print("\n--- Uitslag Lootjes! ---")
for i in range(len(namen_lijst)):
    print(f"{namen_lijst[i]} trekt: {lootjes[i]}")