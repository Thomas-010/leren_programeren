import time, math
import random

player_attack = 1
player_defense = 0
player_health = 3
new_player_health = 0



r1 = random.randint(10,25)
r2 = random.randint(-5,75)
r3 = random.choice(["+", "*", "-"])

def gevecht(attack, defence, health, monster_attack, monster_defence, monster_health):
    print(attack,defence,health)
    zombie_hit_damage = (monster_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
        player_hit_damage = (player_attack -monster_defence)
        player_attack_amount = math.ceil(monster_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        damage = (player_attack_amount * zombie_hit_damage)
        health = health - damage
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {health}.')
        return health
    else:
        print('Helaas is het monster te sterk voor je.')
        print('Game over.')
        exit()
    print('') 
    time.sleep(2)
    return player_health


# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('Je loopt naar de deur toe.')
print('Je opent de deur.')
time.sleep(2)


# === [kamer 7] === #
rupee = 1
print('Je loopt de kamer binnen en je ziet iets glinsteren')
print('Je loopt dichterbij en je ziet dat het een Rupee is en je pakt het op')
print(f"Je hebt nu {rupee} Rupee")
time.sleep(2)

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
if kamer == "kamer 6":
    print('Je gaat door naar kamer 6!')

    time.sleep(2)
    # === [kamer 6] === #
    print(f'Dapper loop je de kamer binnen.')
    print('Je loopt tegen een zombie aan.')
    print(player_health)
    player_health = gevecht(player_attack,player_defense,player_health,1,0,2 )
    print(player_health)


# === [kamer 3] === #
print (player_attack, player_defense)
print('In de kamer zie je een Sneaky Goblin die items verkoopt bij het verkoopverpunt')
print('Je loopt op het verkooppunt af')
print('Je ziet dat je hier items kan kopen zoals een zwaard en een schild!')
print(f'Je ziet dat het zwaard 1 rupee kost en het schild kost ook 1 rupee ')
koop = input('Wil je iets kopen! Zoja wat wil je kopen?')
if koop == "zwaard":
    player_attack += 2
elif koop == "schild":
    player_defense += 1

print (player_attack, player_defense, player_health )


# print('Je duwt hem open en stap een hele lange kamer binnen.')
# print(f'In deze kamer staat een tafel met daarop een {item}.')
# print(f'Je pakt het {item} op en houd het bij je.')
# print('Op naar de volgende deur.')
# print('')
time.sleep(2)

# === [kamer 4] === #
print(f'Dapper loop je de kamer binnen.')
print('Je loopt tegen een goblin aan.')
player_health = gevecht(player_health, player_attack, player_defense, 2,0,3)
time.sleep(2)



# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie of goblin tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel == True:
    print('Je opent de schatkist met de sleutel!')
    print('Je heb de dungeon overleefd en gewonnen')
else:
    print('Je kan de schatkist niet openen je heb verloren')

