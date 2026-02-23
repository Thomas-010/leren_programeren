kaas = input("Is de kaas geel? ja/nee ")

if kaas == "ja":
    kaas = input("Heeft de kaas gaten? ja/nee ")
    if kaas == "ja":
        kaas = input("Is de kaas belachelijk duur? ja/nee ")
        if kaas == "ja":
            print("Emmenthaler")
        else:
            print("Leerdammer")
    else:
        kaas = input("Is de kaas hard als steen? ja/nee ")
        if kaas == "ja":
            print("Parmigiano Reggiano")
        else:
            print("Goudse Kaas")
else:
    kaas = input("Heeft de kaas blauwe schimmels? ja/nee ")
    if kaas == "ja":
        kaas = input("Heeft de kaas een korst? ja/nee ")
        if kaas == "ja":
            print("Bleu de Rochbaron")
        else:
            print("Fourme d'Ambert")
    else:
        kaas = input("Heeft de kaas een korst? ja/nee ")
        if kaas == "ja":
            print("Camembert")
        else:
            print("Mozzarella")