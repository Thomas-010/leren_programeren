print('Welk seizoen vind jij het fijnst?', 
      "a) Lente", 
      "b) Zomer", 
      "c) Herfst", 
      "d) Winter")
gekozen_seizoen = input('? ')

if gekozen_seizoen == 'a' or gekozen_seizoen == 'c':
    print('Dus jij vindt een tussenseizoen het fijnst...')
    weer_type = ''
elif gekozen_seizoen == 'b':
    weer_type = 'warm'
elif gekozen_seizoen == 'd':
    weer_type = 'koud'
else:
     weer_type = ''

if len(weer_type) > 0:
    print(f'Dus jij houd van {weer_type} weer!')
else:
    print('Dit is geen te kiezen optie!')
