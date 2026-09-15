from functions import get_primes_until, get_first_primes, get_primes_between

print("Kies een optie: ")
print("1. Priemgetallen tot en met een getal")
print("2. Een aantal priemgetallen")
print("3. Priemgetallen tussen twee getallen")

keuze = input("Kies een optie:")

if keuze == "1":
    getal = int(input("Voer een getal in: "))
    resultaat = get_primes_until(getal)

elif keuze == "2":
    aantal = int(input("Hoeveel priemgetallen?"))
    resultaat = get_first_primes(aantal)

elif keuze == "3":
    begin = int(input("Vanaf welk getal?"))
    einde = int(input("Tot welk getal?"))
    resultaat =  get_primes_between(begin, einde)

else:
    resultaat = []

if len(resultaat) == 0:
    print("Geen priemgetallen gevonden...")
else:
    print("De gevonden priemgetallen zijn:" , resultaat)