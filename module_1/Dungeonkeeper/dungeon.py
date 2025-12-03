import time, math
import random

player_attack = 1
player_defense = 0
player_health = 3
new_player_health = 0


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
print("Je ziet 2 deuren voor je naar welke kamer ga je?")
kamer1 = input('Kies je voor kamer 2 of kamer 8?')
if kamer1 == "2":
    print('Je gaat door naar kamer 2!')

    # === [kamer 2] === #
    Kamer_6 = bool
    Kamer_2 = bool
    r1 = random.randint(10,25)
    r2 = random.randint(-5,75)
    r3 = random.choice(["+", "*", "-"])

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
    kamer = input('Kies je voor kamer 6 of kamer 8?: ')
    if kamer == "kamer 6":
        print('Je gaat door naar kamer 6!')

        time.sleep(2)
        # === [kamer 6] === #
        print(f'Dapper loop je de kamer binnen.')
        print('Je loopt tegen een zombie aan.')
        print(player_health)
        player_health = gevecht(player_attack,player_defense,player_health,1,0,2 )
        print(player_health)

time.sleep(2)
# === [kamer 8] === #
player_health

print('Welkom bij de gokmachine!')
print("Dit is hoe het werk!")
print("Als de dobbelstenen hoger dan 7 zijn, worden je Rupees verdubbeld!")
print("Als de dobbelstenen lager dan 7 zijn, verlies je 1 health point ")
print("Als de dobbelstenen gelijk aan 7 zijn heb je de jackpot, je krijgt dan 1 Rupees en 4 health points ")
gokken = input('Wil je een poging wagen?: ')
if gokken == "ja":
    while player_health > 0:
        g1 = random.randint(1,6)
        g2 = random.randint(1,6)
        print("Veel succes!")
        print("De goblin gooit de dobbelstenen")
        print(f'De goblin heeft {g1 + g2} gegooid!')
        if g1 + g2 > 7:
            print ('Je heb hoger gegooid dan 7, gefeliciteerd je Rupees worden verdubbeld!')
            rupee *= 2
        elif g1 + g2 == 7:
            print ("Je heb de jackpot, je krijgt 1 Rupees en 4 health erbij!")
            rupee += 1
            player_health += 4
        elif g1 + g2 < 7:
            print ('Je heb lager gegooid dan 7, je verliest 1 health!')
            player_health -= 1
        if player_health == 0:
            print(f"Je health is {player_health}")
            print("Helaas je bent game over!")
            exit()
        opnieuw = input("Wil je nog een keer gokken! ja of nee: ")
        if opnieuw == "ja":
            print (player_health)
            print (gokken)
        else:
            print ("Helaas, tot de volgende keer!")
            print (f"Je heb nu {rupee} Rupees! ")
            print (f"Je heb nu {player_health} health!")
            break
else:
    print ("Helaas dan niet!")

time.sleep(2)
# === [kamer 3] === #
item = ("")
print('In de kamer zie je een Sneaky Goblin die items verkoopt bij het verkoopverpunt')
print('Je loopt op het verkooppunt af')
print('Je ziet dat je hier items kan kopen zoals een zwaard en een schild!')
print('Je ziet dat het zwaard 1 rupee kost en het schild kost ook 1 rupee ')
if rupee >= 2:
    print("Ik voel dat jij meer dan 2 Rupees heb!")
    print("Je moet het zwaard en schild kopen! ")
    player_attack += 2
    player_defense += 1
    item = ("Zwaard en schild")
if rupee == 1:
    item = input("Wil je het zwaard of het schild kopen?: ")
    if item == "zwaard":
        print(f"Je krijgt nu plus 2 attack!")
        item = "zwaard"
        player_attack += 2
    elif item == "schild":
        print(f"Je krijgt plus 1 defence!")
        item = ("schild")
        player_defense += 1



print (player_attack, player_defense, player_health )

time.sleep(2)

# === [kamer 4] === #
print(f'Dapper loop je de kamer binnen met je nieuwe {item}.')
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

