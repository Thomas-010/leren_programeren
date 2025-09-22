from termcolor import colored, cprint, COLORS

woord = 'variable'
{colored(woord, 'yellow', attrs=['bold'])}


croissantjes = int(input('Hoeveel croissantjes?'))
prijsc = int(input('Wat is de prijs van de croissantjes?'))
stokbrood = int(input('Hoeveel stokbroden?'))
prijss = int(input('Wat is de prijs van de stokbroden?'))
kortingsbon3s = int(input('Waarde van kortingsbon'))



totaal = (f'{croissantjes * prijsc + stokbrood * prijss - kortingsbon3s} ')

print(f'De feestlunch kost je bij de bakker {colored(totaal, 'yellow', attrs=['bold'])} voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')