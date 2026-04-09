#defineer hieronder je functies

import random


def geef_willekeurig_getal(eerste: int, laatste: int) -> int:
    "Geeft een willekeurig getal tussen eerste en laatste terug."
    return random.randint(eerste, laatste)

def vraag_gok_aan_speler(ronde: int, beurt: int) -> int:
    "Vraagt de speler om een gok te doen en geeft deze terug."
    "Parameters: ronde = huidige ronde, beurt = huidige beurt"
    return int(input(f'Ronde {ronde}, Beurt {beurt}: Voer je gok in: '))

def controleer_gok(gok: int, geheim: int) -> bool:
    "Controleert of de gok gelijk is aan het geheime getal."
    "Geeft true terug als correct anders false"
    return gok == geheim
    pass

def geef_richtingshint(gok: int, geheim: int) -> str:
    "Geeft een hint of de gok te hoog, te laag of correct is."
    if gok == geheim:
        return 'Geraden'
    elif gok < geheim:
        return 'Hoger'
    else:
        return 'Lager'

def geef_temperatuurhint(gok: int, geheim: int) -> str:
    verschil = abs(gok - geheim)
    "Geeft een hint of de gok warm, koud of heet is."
    
    if verschil < 20:
        return 'Je bent heel warm'
    if verschil < 50:
        return 'Je bent warm'
    else: 
        return '' 

def update_score(score: int, geraden: bool) -> int:
    "Update de score van de speler op basis van de huidige ronde."
    "Voegt 1 punt toe als de speler correct heeft geraden, anders geen punten"
    if geraden:
        return score + 1
    return score
    

def toon_rondescore(ronde: int, score: int):
    "Toont de huidige ronde en de score van de speler."
    "Parameters: score = punten tot nu toe, ronde = gespeelde rondes"
    print(f'Ronde {ronde} is afgelopen. Je score is: {score}')

def toon_eindscore(score: int):
    "Toont de eindscore van de speler na alle rondes."
    print(f'Je eindscore is: {score}')


def vraag_nog_een_keer() -> bool:
    "Vraagt de speler of hij nog een keer wil spelen."
    "Geeft true terug als de speler nog een keer wil spelen, anders false"
    antwoord = input('Wil je nog een keer spelen? (ja/nee): ')
    return antwoord.lower() == 'ja'


#defineer hierboven je functies

if __name__ == "__main__":
    import application

