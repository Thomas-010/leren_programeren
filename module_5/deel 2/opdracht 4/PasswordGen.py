import random, string

speSymbolen = "@#$%&_?"


def test_wachtwoord(ww) -> bool:
    if len(ww) < 24:
        print('te kort')
        return False
    if not 1 < len(list(filter(lambda a: a in string.ascii_uppercase, list(ww)))) < 7:
        print('aantal hoofdletters klopt niet!')
        return False
    if ww[11] in string.ascii_uppercase or ww[12] in string.ascii_uppercase:
        print('In het midden geen hoofdletters')
        return False
    if len(list(filter(lambda a: a in string.ascii_lowercase, list(ww)))) < 8:
        print('te weinig kleine letters')
        return False
    if ww[-1] in string.ascii_lowercase:
        print('Laatste pos niet juist')
        return False
    if len(list(filter(lambda a: a in '@#$%&_?', list(ww)))) != 3:
        print('te weinig specials')
        return False
    if ww[0] in '@#$%&_?' or ww[-1] in '@#$%&_?':
        print('special op end')
        return False
    if not 3 < len(list(filter(lambda a: a.isdigit(), list(ww)))) < 8:
        print('te weinig getallen')
        return False
    if ww[0].isdigit() or ww[1].isdigit() or ww[2].isdigit():
        print('Eerste drie karakters staat een getal')
        return False
    return True



def genereer_wachtwoord():
    aantal_hoofdletters = random.randint(2, 6)
    aantal_specialech = 3
    aantal_cijfers = random.randint(4, 7)
    aantal_kleine_letters = 24 - (aantal_hoofdletters + aantal_specialech + aantal_cijfers)

    tekens = []
    tekens += random.choices(string.ascii_uppercase, k=aantal_hoofdletters)
    tekens += random.choices(speSymbolen, k=aantal_specialech)
    tekens += random.choices(string.digits, k=aantal_cijfers)
    tekens += random.choices(string.ascii_lowercase, k=aantal_kleine_letters)
    
    while True:
        random.shuffle(tekens)
        geldig = True
        
        if tekens[-1] in string.ascii_lowercase:
            geldig = False

        if tekens[0] in speSymbolen or tekens [-1] in speSymbolen:
            geldig = False

        for teken in tekens[:3]:
            if teken in string.digits:
                geldig = False

        for teken in tekens[11:13]:
            if teken in string.ascii_uppercase:
                geldig = False

        if geldig:
            return "".join(tekens)


for i in range(500):
    ww = genereer_wachtwoord()
    if not test_wachtwoord(ww) or len(ww) != 24:
        print('Deze wachtwoorden zijn fout: ')
        print(ww)
        
