print("========================")
print("    DE VERLATEN BUNKER")
print("========================")

zaklamp = False
sleutel = False

print("Je staat voor een oude bunker.")
print("Ga je naar binnen ja of nee?")

keuze = input("Maak een keuze: ").lower()

if keuze =="ja":
    print("Je gaat de bunker binnen.") 

    print("Je ziet twee gangen welke kies je?")
    print("Kies je voor links of rechts?")

    keuze = input("Welke gang kies je?: ").lower()

    if keuze == "links":
        print("Je loopt door de linker gang")
        print("🔦 Je ziet een zaklamp op de grond")
        print("Pak je de zaklamp of op laat je de zaklamp liggen?")

        keuze = input("Pak je de zaklamp op?(ja/nee): ").lower()

        if keuze == "ja":
            zaklamp = True
            print("Je hebt de zaklamp gepakt")
            print("Je kunt de donkere kamer bekijken")
            print("Je loopt naar de donkere kamer")
            print("Ga je naar binnen?")

            keuze = input("Ja of nee?: ").lower()

            if keuze == "ja":
                print("Je doet de zaklamp aan")
                print("🚪 Je ziet een gang met twee deuren")
                print("Ga je naar links of rechts")

                keuze = input("Links of rechts?: ").lower()

                if keuze == "links":
                    print("Je opent de deur")
                    print("De deur valt achter je dicht")
                    print("Je zit vast!")
                    print("💀 GAME OVER")

                elif keuze == "rechts":
                    print("Je opent de deur")
                    print("Je vindt een trap naar beneden")
                    print("Je loopt de trap af naar beneden")

                    print("Je komt beneden bij een splitsing")
                    print("Je ziet twee tunnels")
                    print("Ga je naar links of rechts?")

                    keuze = input("Links of rechts?:").lower()

                    if keuze == "links":
                        print("Je loopt door de linker tunnel.")
                        print("De tunnel wordt steeds smaller en je kan niet meer verder")
                        print("💀 GAME OVER")

                    elif keuze == "rechts":
                        print("Je loopt door de rechter tunnel")
                        print("Je ziet een oude nooduitgang")
                        print("De deur zit op slot")
                        print("Wil je deze openen")

                        keuze = input("Ja of nee?: ").lower()

                        if keuze == "ja" and sleutel == True:
                                print("Je opent de nooduitgang")
                                print("Je bent ontsnapt uit de bunker!")
                                print("🎉 GEWONNEN")
                        else: 
                                print("Je hebt geen sleutel")
                                print("Je kunt de deur niet openen")
                                print("💀 GAME OVER")
                    else:
                            print("Dat is geen geldige keuze")
                else:
                    print("Je loopt weg van de donkere kamer!")
            else:
                print("Je laat de zaklamp liggen")
                print("Het is veel te donker")
                print("Je verdwaalt")
                print("💀 Game over")
        else:
            print("Je laat de zaklamp liggen")
            print("Het is veel te donker")
            print("Je verdwaalt")
            print("💀 Game over")

    

    elif keuze == "rechts":
        print("Je loopt door de rechter gang")
        print("Je vindt een oude opslagruimte")

        keuze = input("Ga je naar binnen of loop je verder: ").lower()

        if keuze == "ja":
            print("Je ziet oude dozen. Ga je ze doorzoeken?")

            keuze = input("Ga je de dozen doorzoeken? ").lower()

            if keuze == "ja":
                print("🔑 Je vindt een sleutel")
                sleutel = True
                print("Je loopt verder")

                print("Je ziet een grote deur")
                print("De deur zit op slot wil je deze openen?")

                keuze = input("Ja of nee?: ").lower()

                if keuze == "ja":
                    if sleutel == True:
                        print("Je gebruikt de sleutel en de deur gaat open!")
                        print("Je bent onstanpt uit de bunker!")
                        print("🎉 GEWONNEN")
                    else:
                        print("Je heb geen sleutel om de deur te openen")
                else:
                    print("Je loopt weg van de deur")
    else:
        print("Dat is geen geldige keuze")

else:
    print("Je besluit de bunker niet binnen te gaan!")
    print("Je avontuur is voorbij! Doei")        
    