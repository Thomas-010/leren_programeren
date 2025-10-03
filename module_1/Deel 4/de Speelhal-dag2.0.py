from termcolor import colored, cprint, COLORS
import termcolor
toegang_ticket_euro = float(input("vul hier de prijs van 1 toegang ticket in: "))
toegang_ticket = int(round(toegang_ticket_euro * 100))
vr_euro = float(input("vul hier de prijs van 5 minuten vr: "))
vr_tijd = int (input ("vul hier in hoelang je in de vr wilt in minuten: "))
vr_tijd_omgerekend = int(round(vr_tijd / 5))
vr = int(round(vr_euro * 100))
personen = int(input("vul hier de hoeveel personen mee gaan: "))



totaal = (toegang_ticket * personen) + (vr * vr_tijd_omgerekend * personen)
totaal2 = int(round(totaal / 2))

print (totaal)

print(f"Dit geweldige dagje-uit met {colored(personen, 'blue')} mensen in de Speelhal met {colored(vr_tijd, 'green')} minuten VR kost je maar {colored(totaal2, 'red')} eurocent per persoon voor 2 mensen")