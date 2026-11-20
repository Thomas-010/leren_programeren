import data
import functions

def main():
    print(data.WELKOMSTTEKST)

    doorgaan = True

    while doorgaan:
        aantal = functions.vraag_aantal_bolletjes()

        verpakking = functions.vraag_verpakking(aantal)

        functions.toon_bestelling(aantal, verpakking)

        doorgaan = functions.vraag_nog_een_bestelling()

    print(data.BEDANKT)

main()