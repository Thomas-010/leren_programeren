import random, string

speSymbolen = "@#$%&_"

def is_geldig(tekens):
    if tekens[-1] in string.ascii_lowercase:
        return False

    if tekens[0] in speSymbolen or tekens [-1] in speSymbolen:
        return False

    for teken in tekens[:3]:
        if teken in string.digits:
            return False

    for teken in tekens[11:13]:
        if teken in string.ascii_uppercase:
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
        if is_geldig(tekens):
            return "".join(tekens)
        
#Verbetering krijg ik mee: Volgende keer een aparte functie maken voor het controleren van de geldigheid van het wachtwoord.


nieuw_wachtwoord = genereer_wachtwoord()
print(nieuw_wachtwoord)