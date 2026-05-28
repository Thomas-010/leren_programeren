from functions import *

# De flow van je programma
def main():
    score = 0
    ronde = 1
    geheim = geef_willekeurig_getal(1, 1000)

    geraden = False
    beurt = 0

    while not geraden:
        beurt +=1 
        gok = vraag_gok_aan_speler(ronde, beurt)

        geraden = controleer_gok(gok, geheim)


        score = update_score(score, geraden)
        
        print (geef_richtingshint(gok, geheim))
        
        temp = geef_temperatuurhint(gok, geheim)
        if temp != '':
            print(temp)

    score = update_score(score, geraden)
    toon_rondescore(ronde, score)

# voer de flow uit
main()