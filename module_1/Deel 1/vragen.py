Naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
jongemeisje = input("Ben je een A) een jonge of B) een meisje? ").lower()
favokleur = input("Wat is je favoriete kleur? ")
favogetal = int(input("Wat is je favoriete getal? "))
getal = abs(leeftijd-favogetal)
verschil = 'haar' if jongemeisje == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", Naam)
print(f"{verschil.capitalize()} leeftijd is:", leeftijd)
print(f"{Naam}'s favoriete kleur is:", favokleur)
print(f"Het verschil tussen {verschil} leeftijd en {favogetal} is:", getal)




