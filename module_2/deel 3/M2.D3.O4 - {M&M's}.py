import random

kleuren = ('Rood', 'blauw', 'groen', 'geel', 'bruin')

hoeveel = int(input("Hoeveel M&M's wilt u toevoegen aan de zak? "))

zak = {}

for i in range(hoeveel):
    kleur = random.choice(kleuren)
    if kleur in zak:
        zak[kleur] += 1
    else:
        zak[kleur] = 1


print(f"Je zak met M&M's bevat nu:", zak)

