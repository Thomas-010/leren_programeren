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

if cijfer < 1 or cijfer > 10:
    print('Dit kan ik niet omzetten!')
elif 6 >= cijfer:
    print (f"Gefeliciteerd, {beschrijving[cijfer_afgerond]} je resultaat is een {cijfer}")
else: 6 <= cijfer
print (f"Jammer, {beschrijving[cijfer_afgerond]} je resultaat is een {cijfer}")


