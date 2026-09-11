from vraag_gegevens import verzamel_gegevens

personen = verzamel_gegevens()

for persoon in personen:
    print(f"{persoon['name']}, die in {persoon['city']} woont, is {persoon['age']} jaar")