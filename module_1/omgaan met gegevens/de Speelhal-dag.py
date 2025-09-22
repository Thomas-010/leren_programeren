
from termcolor import colored

vrienden = 5.00
toegang = 7.45
vr = 16.65
totaalbedrag = 29.10


totaal = (f'{(vrienden + toegang + vr) / 2} ')

print (f'Dit geweldige dagje-uit met 5 mensen in de Speelhal met 45 minuten VR kost je maar {colored(totaal, 'yellow', attrs=['bold'])} euro per persoon voor 2 mensen')