totaal = 50
huidig_getal = 51
herhaal = 0
reeks = "50"

print(f"{herhaal} + {reeks} = {totaal}")

while totaal <= 1000:
    herhaal += 1
    reeks += f" + {huidig_getal}"
    totaal += huidig_getal
    herhaal += 1
    print(f'{herhaal}. {reeks} = {totaal}')
    huidig_getal += 1
