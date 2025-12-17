# name of student: Thomas
# number of student: 99074704
# purpose of program: Helpen met uitrekenen hoeveel wisselgeld gegeven moet worden
# structure of program: Vraagt betaalde bedrag en gegeven bedrag, berekent het wisselgeld en een lijst met wisselgeld dat is teruggegeven

coinValues = [500,200,100,50,20,10,5,2,1] # Lijst van munten in centen groot naar klein

toPay = int(float(input('Amount to pay: '))* 100) # Dit vraagt het te betalen bedrag en zet het om naar centen
paid = int(float(input('Paid amount: ')) * 100) # Dit vraagt het betaalde bedrag en zet het om naar centen
change = paid - toPay # Dit berekent het wisselgeld

Coinsterug = {} #zelf toegevoegd

while change > 0 and len(coinValues) > 0: # Dit loopt door de door de lijst tot er geen wisselgeld meer is of alle munten gebruikt zijn
  coinValue = coinValues.pop(0) # Dit haalt de eerste munt uit de lijst en geeft hem terug
  nrCoins = change // coinValue # Dit berekent het maximale geld wat terug gegeven kan worden van elke munt

  if nrCoins > 0: # Wordt alleen uitgevoerd als minstens een munt nodig is
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Geeft aan hoeveel munten maximaal teruggegeven kunnen worden
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Dit vraagt hoeveel munten door de gebruiker terug gegeven zijn.
    change -= nrCoinsReturned * coinValue # Dit haalt het teruggegeven bedrag van het wisselgeld af
    Coinsterug[coinValue] = nrCoinsReturned #Zelf toegevoegd

if change > 0: # Dit controleert of er nog wisselgeld over is 
  print('Change not returned: ', str(change) + ' cents') # Geeft aan dat niet al het wisselgeld is teruggegeven
else:
  print('done')


print('Returned coins! ') # Zelf toegevoegd
for coin, nr in Coinsterug.items():
  print(f"{nr} coins of {coin} cents")