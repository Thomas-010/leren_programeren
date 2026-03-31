#defineer hieronder je functies

def geef_willekeurig_getal(eerste: int, laatste: int) -> int:
    "Geeft een willekeurig getal tussen eerste en laatste terug."
    pass

def vraag_gok_aan_speler(ronde: int, beurt: int) -> int:
    "Vraagt de speler om een gok te doen en geeft deze terug."
    "Parameters: ronde = huidige ronde, beurt = huidige beurt"
    pass

def controleer_gok(gok: int, geheim: int) -> bool:
    "Controleert of de gok gelijk is aan het geheime getal."
    "Geeft true terug als correct anders false"
    pass

def geef_richtingshint(gok: int, geheim: int) -> str:
    "Geeft een hint of de gok te hoog, te laag of correct is."
    pass

def geef_temperatuurhint(gok: int, geheim: int) -> str:
    "Geeft een hint of de gok warm, koud of heet is."
    pass

def update_score(score: int, geraden: bool) -> int:
    "Update de score van de speler op basis van de huidige ronde."
    "Voegt 1 punt toe als de speler correct heeft geraden, anders geen punten"
    pass

def toon_rondescore(ronde: int, score: int):
    "Toont de huidige ronde en de score van de speler."
    "Parameters: score = punten tot nu toe, ronde = gespeelde rondes"
    pass

def toon_eindscore(score: int):
    "Toont de eindscore van de speler na alle rondes."
    pass

def vraag_nog_een_keer() -> bool:
    "Vraagt de speler of hij nog een keer wil spelen."
    "Geeft true terug als de speler nog een keer wil spelen, anders false"
    pass


#defineer hierboven je functies

if __name__ == "__main__":
    import application

