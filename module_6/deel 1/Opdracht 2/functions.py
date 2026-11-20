import data


def vraag_aantal_bolletjes():
    while True:
        aantal = input(data.VRAAG_AANTAL)

        if aantal.isdigit():
            aantal = int(aantal)

            if data.MIN_BOLLETJES <= aantal <= data.MAX_BOLLETJES:
                return aantal

            elif aantal > data.MAX_BOLLETJES:
                print(data.FOUT_GROOT)
        else:
            print(data.FOUT_INVOER)

def vraag_verpakking(aantal):
    if aantal >= 4:
        print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes vanille ijs.')
        return 'bakje'
    
    
    while True:
        verpakking = input(data.VRAAG_VERPAKKING.format(aantal).lower().strip())

        if verpakking == 'hoorntje' or verpakking == 'bakje':
            return verpakking

        print(data.FOUT_INVOER)
        

def toon_bestelling(aantal, verpakking):
    print(f'Hier is uw {verpakking} met {aantal} bolletjes vanille ijs.')


def vraag_nog_een_bestelling():
    while True:
        antwoord = input(data.VRAAG_OPNIEUW).lower().strip()

        if antwoord == 'ja':
            return True
        elif antwoord == 'nee':
            return False

        print(data.FOUT_INVOER)
    


