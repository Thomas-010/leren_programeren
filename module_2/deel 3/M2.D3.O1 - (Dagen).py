dagen_tuple = ('Maandag', 'Dinsdag', 'Woensdag', 'Donderdag','Vrijdag', 'Zaterdag','Zondag')

print('\nAlle dagen van de week zijn:')
for dag in dagen_tuple:
    print(f'- {dag}')

print(f'\nDe weekenddagen zijn: {dagen_tuple[5]} en {dagen_tuple[6]}')

werkdagen = dagen_tuple[0:5]
print(f'\nDe werkdagen zijn: {werkdagen[0]}, {werkdagen[1]}, {werkdagen[2]}, {werkdagen[3]} & {werkdagen[4]}')

omgekeerd = dagen_tuple[::-1]
print(f'\nAlle dagen van de week in omgekeerde volgorde zijn: {'->'.join (omgekeerd)}.')

print('\nDe werkdagen in omgekeerde volgorde zijn:')
for dag in werkdagen[::-1]:
    print(f'- {dag}')

print(f'\nDe weekenddagen in omgekeerde volgorde zijn: {dagen_tuple[6]} & {dagen_tuple[5]} ')
