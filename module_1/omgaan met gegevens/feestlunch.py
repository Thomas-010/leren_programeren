from termcolor import colored, cprint, COLORS

woord = 'variable'
{colored(woord, 'yellow', attrs=['bold'])}


croissantjes = 17
prijsc = 0.37
stokbrood = 2
prijss = 2.38
kortingsbon3s = 1.50



totaal = (f'{croissantjes * prijsc + stokbrood * prijss - kortingsbon3s} ')

print(f'De feestlunch kost je bij de bakker {colored(totaal, 'yellow', attrs=['bold'])} voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')