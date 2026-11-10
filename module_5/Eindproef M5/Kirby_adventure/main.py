from termcolor import colored
from data import KEUZES, MAGENTA
from functions import *

def main():
    print('Welkom bij de text adventure')

    print(colored("⭐ kirby en het verdwenen sterrenkristal ⭐", "magenta"))
    print("kirby moet dream land redden!")
    print("vind het sterrenkristal en versla king dedede\n")

    print("1. kirby staat bij een bos en een grot")

    keuze = vraag_keuze(
        'Ga je naar het bos of de grot?',
        KEUZES['bos_of_grot']
    )

    if keuze == 'bos':
        voorwerpen = speel_bos()
    else:
        voorwerpen = speel_grot()


    heeft_sleutel = voorwerpen["heeft_sleutel"]
    heeft_magische_ster = voorwerpen["heeft_magische_ster"]

    speel_kasteel(heeft_sleutel)
t
    eindgevecht(heeft_magische_ster)


if __name__ == "__main__":
    main()