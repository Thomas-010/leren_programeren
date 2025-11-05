import time, math
import random

player_attack = 1
player_defense = 0
player_health = 3
new_player_health = 0



r1 = random.randint(10,25)
r2 = random.randint(-5,75)
r3 = random.choice(["+", "*", "-"])

def gevecht(attack, defence, health):
    zombie_hit_damage = (attack - player_defense)
    new_player_health = (attack - player_health)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
        player_hit_damage = (player_attack - defence)
        player_attack_amount = math.ceil(health / player_hit_damage)

    if player_attack_amount <= zombie_attack_amount:
        damage = (player_attack_amount * zombie_hit_damage)
        new_player_health = max(0, player_health - damage)
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {new_player_health}.')
        return new_player_health
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
    print('') 
    time.sleep(1)
    return player_health


# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('Je loopt naar de deur toe.')
print('Je opent de deur.')
time.sleep(1)

# === [kamer 2] === #
Kamer_6 = bool
Kamer_2 = bool

print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
print(f'Daarboven zie je een som staan {r1} {r3} {r2}')
antwoord = int(input('Wat toets je in?'))

if r3 == "+":
    goed = r1 + r2
elif r3 == "*":
    goed = r1 * r2
elif r3 == "-":
    goed = r1 - r2

if antwoord == goed:
    print(f'Het stadbeeld laat de sleutel vallen en je pakt het op')
    sleutel = True
else:
    print('Er gebeurt niets....')
    sleutel = False

print('Je ziet twee deuren voor je')
print('Een deur gaat naar kamer 6')
print('De andere deur gaat naar kamer 3')
print('Door welke deur ga je heen?')
kamer = input('Kies je voor kamer 6 of kamer 3?')
if kamer == "Kamer 6":
    print('Je gaat door naar kamer 6!')

    time.sleep(1)
    # === [kamer 6] === #
    print(f'Dapper loop je de kamer binnen.')
    print('Je loopt tegen een zombie aan.')
    player_health = gevecht(1,0,2)



# === [kamer 3] === #
item = random.choice(["Zwaard", "Schild"])
if item == "Zwaard":
    player_attack += 2
elif item == "Schild":
    player_defense += 1

print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #
print(f'Dapper loop je de kamer binnen.')
print('Je loopt tegen een goblin aan.')
player_health = gevecht(2,0,3)



# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie of goblin tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel == True:
    print('Je opent de schatkist met de sleutel!')
    print('Je heb de dungeon overleefd en gewonnen')
else:
    print('Je kan de schatkist niet openen je heb verloren')

