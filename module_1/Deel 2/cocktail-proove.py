cocktails = {
    "Negroni": ["Gin", "Rode Vermouth", "Campari"],
    "Mojito": ["Witte Rum", "Limoensap", "Munt", "Suiker", "Sodawater"],
    "Kir": ["Witte Wijn", "Crème de Cassis"],
    "White Lady": ["Gin", "Cointreau", "Citroensap"],
    "Spritz": ["Prosecco", "Aperol", "Sodawater"],
    "Fizz": ["Gin", "Citroensap", "Suiker", "Sodawater"],
    "French Martini": ["Chambord", "Vodka", "Ananassap"],
    "French Connection": ["Amaretto", "Cognac"]
}


def toon_cocktail(naam):
    print(f"\nJouw cocktail is: {naam}!")
    print("Ingrediënten:")
    for ingr in cocktails[naam]:
        print(f" - {ingr}")

#begin
rood = input('Zit er rood in je drank? [ja/nee]:').strip().lower()

if rood == "ja":
    bruis = input("Zit er bubbels in je drankje [ja/nee]").strip().lower()
    if bruis == "ja":
        bitter = input("Is je drankje bitter [ja/nee]").strip().lower()
        if bitter == "ja":
            toon_cocktail('Spritz')
        else:
            toon_cocktail('Kir')
    else:
        sterk = input ('Wordt je cocktail als sterk/klassiek ervaren? [ja/nee]]').strip().lower()
        if sterk == 'ja':
            toon_cocktail('Negroni')
        else:
            toon_cocktail('French Martini')
else:
    kleur = input('Is je cocktail helder/lichtgeel? [ja/nee]').strip().lower()
    if kleur == 'ja':
        toon_cocktail('White Lady')
    else:
        toon_cocktail('French Connection')
        

