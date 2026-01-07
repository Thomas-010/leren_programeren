wachtwoord = "school"
poging = 0
max_aantal = 5
juist_wachtwoord = True

while poging < max_aantal:
    invoer = input("Voet het wachtwoord in: ")
    poging += 1
    
    if invoer == wachtwoord:
        print(f"Je heb het wachtwoord juist geraden {poging} poging(en)! ")
        break
else:
    print('Je mag niet meer inloggen ')

