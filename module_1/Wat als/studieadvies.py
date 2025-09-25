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


for nummer, stelling in enumerate(stellingen, start=1):
    print(f'\nStelling {nummer}:, {stelling}')
    antwoord = int(input(OPTIES + ''))
    totaal_score += antwoord

aantal_stelling = len(stellingen)
gemiddelde = totaal_score / aantal_stelling

print (COMPETENTIE_ADVIES_TITEL)
print(f"Jouw totaalscore: {totaal_score} (gemiddelde: {gemiddelde:.1f})")

if gemiddelde <= 2:
    print (COMPETENTIE_ADVIES_ZORGELIJK)
elif gemiddelde <= 3:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)



