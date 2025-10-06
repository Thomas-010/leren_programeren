from studieadviestext import *

print (STUDIEDOKTER_TITEL)

weken = int(input(AANTAL_WEKEN_VRAAG + ""))



stellingen = [
    COMPETENTIE_STELLING_1,
    COMPETENTIE_STELLING_2,
    COMPETENTIE_STELLING_3,
    COMPETENTIE_STELLING_4,
    COMPETENTIE_STELLING_5,
]

if weken >= 10:
    stellingen.append(COMPETENTIE_STELLING_6)
    stellingen.append(COMPETENTIE_STELLING_7)

totaal_score = 0
count_altijd = 0  
count_vaak = 0
count_regelmatig = 0


for nummer, stelling in enumerate(stellingen, start=1):
    print(f'\nStelling {nummer}:, {stelling}')
    antwoord = int(input(OPTIES + ''))
    totaal_score += antwoord

    if antwoord == 1:
        count_altijd += 1
    elif antwoord == 2:
        count_vaak += 1
    elif antwoord == 3:
        count_regelmatig

aantal_stelling = len(stellingen)
gemiddelde = totaal_score / aantal_stelling

print (COMPETENTIE_ADVIES_TITEL)
print(f"Jouw totaalscore: {totaal_score} (gemiddelde: {gemiddelde:.1f})")
print(f"Aantal keer 'altijd': {count_altijd}")
print(f"Aantal keer 'vaak': {count_vaak}")
print(f"Aantal keer 'regelmatig': {count_regelmatig}")

altijd_vaak = (count_altijd + count_vaak) > (aantal_stelling / 2)
altijd_vaak_regelmatig = (count_altijd + count_vaak + count_regelmatig) > (aantal_stelling / 2)


if gemiddelde <= 2 or altijd_vaak:
    print (COMPETENTIE_ADVIES_ZORGELIJK)
elif gemiddelde <= 3 or altijd_vaak_regelmatig:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)



