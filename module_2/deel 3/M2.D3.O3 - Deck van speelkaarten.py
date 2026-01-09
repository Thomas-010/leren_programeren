import random

speelkaart = ['Harten', 'Klaveren', 'Schoppen', 'Ruiten']
kaart = ['Aas', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Heer']
joker = ['Joker', 'Joker']

deck = []


for k in kaart:
    for s in speelkaart:
        deck.append(f'{s} {k}')
deck.extend(joker)
random.shuffle(deck)

for i in range(7):
    print(f'Kaart {i+1}: {deck[i]}')

andere = deck[7:]
print(f'\nDeck ({len(deck)} kaarten): {andere})')