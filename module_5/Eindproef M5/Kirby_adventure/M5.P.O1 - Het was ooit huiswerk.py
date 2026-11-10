print('welkom bij de text adventure')
 
from termcolor import colored
 
print(colored("⭐ kirby en het verdwenen sterrenkristal ⭐", "magenta"))
print("kirby moet dream land redden!")
print("vind het sterrenkristal en versla king dedede\n")
 
sleutel = 0
kristal = 0
 
print("1. kirby staat bij een bos en een grot")
keuze = input("ga je naar het bos of de grot? ")
 
if keuze == "bos":
    print("kirby loopt het bos in en ziet een gouden sleutel liggen")
    keuze = input("pak je de sleutel? ja of nee ")
 
    if keuze == "ja":
        sleutel += 1
        print("je hebt de gouden sleutel gevonden!")
    else:
        print("kirby loopt verder zonder sleutel")
 
    print("een waddle dee komt naar je toe")
    keuze = input("vechten of vluchten? ")
 
    if keuze == "vechten":
        print("kirby wint het gevecht en vindt een magische ster")
        kristal += 1
    elif keuze == "vluchten":
        print("kirby rent weg en komt bij het kasteel")
    else:
        print("kirby twijfelt te lang en de vijand verslaat hem")
        print(colored("game over!", "red"))
        exit()
 
elif keuze == "grot":
    print("kirby loopt een donkere grot in")
    keuze = input("ga je links of rechts? ")
 
    if keuze == "links":
        print("kirby vindt een magische ster")
        kristal += 1
    elif keuze == "rechts":
        print("kirby valt in een diepe afgrond")
        print(colored("game over!", "red"))
        exit()
    else:
        print("kirby verdwaalt in de grot")
        print(colored("game over!", "red"))
        exit()
 
else:
    print("kirby blijft staan en wordt overvallen door een vijand")
    print(colored("game over!", "red"))
    exit()
 
print("\nkirby komt aan bij het kasteel")
print("er staat een grote deur")
 
keuze = input("wil je de deur openen of een andere ingang zoeken? ")
 
if keuze == "openen":
    if sleutel > 0:
        print("de gouden sleutel opent de deur")
    else:
        print("de deur zit op slot")
        keuze = input("probeer je de deur in te trappen? ja of nee ")
 
        if keuze == "ja":
            print("de deur valt om maar een bewaker pakt kirby")
            print(colored("game over!", "red"))
            exit()
        else:
            print("kirby zoekt een andere ingang")
 
elif keuze == "andere ingang":
    print("kirby klimt door een open raam naar binnen")
 
else:
    print("kirby loopt verkeerd en komt vast te zitten")
    print(colored("game over!", "red"))
    exit()
 
print("\nkirby ziet king dedede met het sterrenkristal")
keuze = input("vechten of praten? ")
 
if keuze == "vechten":
    if kristal > 0:
        print("de magische ster geeft kirby extra kracht!")
        print("kirby verslaat king dedede en pakt het sterrenkristal")
        print(colored("🎉 kirby heeft gewonnen en dream land is gered!", "green"))
    else:
        print("king dedede is te sterk voor kirby")
        print(colored("game over!", "red"))
 
elif keuze == "praten":
    print("king dedede wil het kristal alleen teruggeven als kirby hem verslaat")
    keuze = input("accepteer je de uitdaging? ja of nee ")
 
    if keuze == "ja":
        if kristal > 0:
            print("kirby gebruikt de magische ster en wint!")
            print(colored("🎉 dream land is gered!", "green"))
        else:
            print("kirby probeert te vechten maar verliest")
            print(colored("game over!", "red"))
    else:
        print("kirby geeft op en blijft opgesloten in het kasteel")
        print(colored("game over!", "red"))
 
else:
    print("kirby doet niets en king dedede sluit hem op")
    print(colored("game over!", "red"))