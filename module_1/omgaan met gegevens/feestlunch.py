from termcolor import colored, cprint, COLORS

woord = 'variable'
{colored(woord, 'yellow', attrs=['bold'])}


croissantjes = int(input('Hoeveel croissantjes?'))
croissantjes_cent = int(round(croissantjes *100))
prijsc = int(input('Wat is de prijs van de croissantjes?'))
stokbrood = int(input('Hoeveel stokbroden?'))
stokbrood_cent = int(round(stokbrood * 100))
prijss = int(input('Wat is de prijs van de stokbroden?'))
kortingsbon = int(input('Waarde van kortingsbon'))
kortingsbonx3 = int(round(kortingsbon * 100))
aantalkortingsbon = int(round(kortingsbon))

totaal = (croissantjes_cent * croissantjes)  + (stokbrood_cent * stokbrood) -  (aantalkortingsbon * kortingsbonx3) 


print(f'De feestlunch kost je bij de bakker {colored(totaal, 'yellow', attrs=['bold'])} voor de {croissantjes} croissantjes en de {stokbrood} stokbroden als de {kortingsbonx3} kortingsbonnen nog geldig zijn!')

