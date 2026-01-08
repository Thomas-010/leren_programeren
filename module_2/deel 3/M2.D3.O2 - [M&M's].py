import random

kleur = ('Oranje', 'Blauw', 'Groen', 'Bruin')

hoeveel = int(input("Hoeveel M&M's wilt u toevoegen aan de zak? "))

MMS = []

for m in range(hoeveel):
    MMS.append(random.choice(kleur))

print(', '.join(MMS))
