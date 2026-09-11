from vraag_gegevens import verzamel_gegevens
import termcolor

personen = verzamel_gegevens()

for persoon in personen:
    naam_colored = termcolor.colored(persoon['name'], 'green')
    stad_colored = termcolor.colored(persoon['city'], 'yellow')
#   leeftijd_colored = termcolor.colored(str(persoon['age']), 'yellow')
    
    if persoon['is_volwassen']:
        jaren_volwassen = int(persoon['age']) - 18
        tekst_volwassen = f"al {jaren_volwassen} jaar volwassen"   
    else:
        tekst_volwassen = "nog niet volwassen"

    volwassen_colored = termcolor.colored(tekst_volwassen, 'red')

    print(f"In {stad_colored} woont {naam_colored}, die al {volwassen_colored} is.")