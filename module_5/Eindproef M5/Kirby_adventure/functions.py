from termcolor import colored
from data import ROOD, GROEN, KEUZES

def vraag_keuze(vraag, opties): # Stelt een vraag en blijft vragen tot de speler een geldige optie typt
    while True:
        keuze = input(vraag + ': ').strip().lower()

        if keuze in opties:
            return keuze

        print('Ongeldige keuze. Probeer opnieuw!')


def toon_einde(bericht, kleur): # Laat een eindbericht in een kleur zien en stopt het programma
    print(colored(bericht, kleur))
    raise SystemExit


def game_over(): # Eindigt het spel met een rood 'Game over!' bericht
    toon_einde('Game over!', ROOD)

def gewonnen(bericht): # Eindigt het spel met een groen winbericht
    toon_einde(bericht, GROEN)

def speel_bos():
    # Het bos-pad: Kirby kan een sleutel pakken en tegen een Waddle Dee vechten
    # Geeft terug of Kirby de sleutel en de magische ster heeft
    print('Kirby loopt het bos in en ziet een gouden sleutel liggen')

    keuze = vraag_keuze(
        "Pak je de sleutel? ja of nee",
        KEUZES['ja_nee']
    )

    if keuze == 'ja':
        print('Je hebt de gouden sleutel gevonden!')
        heeft_sleutel = True
    else:
        print('Kirby loopt verder zonder sleutel')
        heeft_sleutel = False

    print('Een Waddle Dee komt naar je toe')

    keuze = vraag_keuze(
        "Vechten of vluchten?",
        KEUZES['vechten_vluchten']
    )

    if keuze == 'vechten':
        print('Kirby wint het gevecht en vindt een magische ster')
        heeft_magische_ster = True
    else:
        print('Kirby rent weg en komt bij het kasteel')
        heeft_magische_ster = False

    return {
        'heeft_sleutel': heeft_sleutel,
        'heeft_magische_ster': heeft_magische_ster
    }




def speel_grot():
    # Het grot-pad: links geeft een magische ster, rechts is game over
    # Er is geen sleutel in de grot, dus die is altijd False
    print('Kirby loopt een donkere grot in')

    keuze = vraag_keuze(
        "Ga je links of rechts?",
        KEUZES['links_rechts']
    )

    if keuze == 'links':
        print('Kirby vindt een magische ster')
        heeft_magische_ster = True
    else:
        print('Kirby valt in een diepe afgrond')
        game_over()

    return {
        'heeft_sleutel': False,
        'heeft_magische_ster': heeft_magische_ster
    }


def speel_kasteel(heeft_sleutel):
     # Het kasteel: Kirby moet naar binnen met de sleutel of via een andere ingang
    print('\nKirby komt aan bij het kasteel')
    print('Er staat een grote deur')

    keuze = vraag_keuze(
        "Wil je de deur openen of een andere ingang zoeken?(openen/andere ingang)",
        KEUZES['kasteel']
    )

    if keuze == 'openen':
        if heeft_sleutel:
            print('De gouden sleutel opent de deur')
        else:
            print('De deur zit op slot!')

            keuze = vraag_keuze(
                'Probeer je de deur in te trappen? ja of nee ',
                KEUZES['ja_nee']
            )

            if keuze == 'ja':
                print('De deur valt om maar een bewaker pakt Kirby')
                game_over()

            print('Kirby zoekt een andere ingang')

    else:
        print('Kirby klimt door een open raam naar binnen')

def eindgevecht(heeft_magische_ster): 
    # Het laatste gevecht tegen King Dedede
    # Met de magische ster win je, zonder de ster is het game over
    print('\nKirby ziet king dedede met het sterrenkristal')

    keuze = vraag_keuze(
        'vechten of praten? ',
        KEUZES['vechten_praten']
    )

    if keuze == 'praten':
        print('King dedede wil het kristal alleen teruggeven als Kirby hem verslaat')

        keuze = vraag_keuze(
            'accepteer je de uitdaging? ja of nee ',
            KEUZES['ja_nee']
        )

        if keuze == 'nee':
            print('Kirby geeft op en blijft opgesloten in het kasteel!')
            game_over()

    if heeft_magische_ster:
        if keuze == 'vechten':
            print('De magische ster geeft Kirby extra kracht!')
            print('Kirby verslaat king dedede en pakt het sterrenkristal')
            gewonnen('🎉 kirby heeft gewonnen en dream land is gered!')
        else:
            print("kirby gebruikt de magische ster en wint!")
            gewonnen("🎉 dream land is gered!")
    
    
    else: 
        if keuze == 'vechten':
            print('King dedede is te sterk voor Kirby')
        else: 
            print('Kirby probeert te vechten maar verliest')

        game_over()