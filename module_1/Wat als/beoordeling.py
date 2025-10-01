cijfer = float(input('Voer hier de eind cijfer van je toets in: '))
cijfer_afgerond = int(round(cijfer , 1))
beschrijving = [
'invalid',
'zeer slecht',
'slecht',
'gerig',
'onvoldoende',
'bijna voldoende',
'voldoende',
'ruim voldoende',
'goed',
'zeer goed',
'uitmuntend',
]
print(cijfer)
if cijfer < 1 or cijfer > 10:
    print('Dit kan ik niet omzetten!')
elif cijfer >= 6:
    print (f"Gefeliciteerd, {beschrijving[cijfer_afgerond]} je resultaat is een {cijfer}")
else:
    print (f"Jammer, {beschrijving[cijfer_afgerond]} je resultaat is een {cijfer}")


