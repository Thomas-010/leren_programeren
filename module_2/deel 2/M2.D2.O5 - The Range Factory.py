aantal_lijst = int(input('Hoeveel lijstjes wil je zien?'))
lijst = []

for i in range(1, aantal_lijst + 1):
    lengte = int(input(f'Hoelang moet lijst {1} zijn?'))
    lijst2 = []
    
    for n in range(lengte):
        lijst2.append(i * (n + 1))
    lijst.append(lijst2)

for lst in lijst:
    print (lst, end='')