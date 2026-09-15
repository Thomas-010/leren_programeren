def is_even(getal:int) -> bool:
    return getal % 2 == 0

#print(is_even(4))
#Kijkt of het getal even is


def draait_woorden_om(tekst:str) -> str:
    woorden = tekst.split()
    omgedraaide_woorden = woorden[::-1]
    omgekeerde_zin = ' '.join(omgedraaide_woorden)
    return omgekeerde_zin

#print(draait_woorden_om("Hallo ik ben een papegaai"))
#Dit draait de worden om die je invoert

def tel_unieke_letter(tekst:str) -> int:
    unieke_tekens = set(tekst)
    aantal_unieke_tekens = len(unieke_tekens)
    return aantal_unieke_tekens

#print(tel_unieke_letter("Hallo ik ben een papegaai"))
#Telt de unieke letters in de zin die ik invoer

def ber_gemiddelde_woordlenge(zin:str) -> float:
    woorden = zin.split()
    
    totaal_aant_tekens = 0
    for letters in woorden:
        totaal_aant_tekens += len(letters)

    gemiddelde_lengte = totaal_aant_tekens / len(woorden)
    return gemiddelde_lengte

#print(ber_gemiddelde_woordlenge("Hallo ik ben een papegaai"))
# Dit berekent het gemiddelde van de zin die je invoert

def vermenigvuldigingstafel(getal:int, aantal:int=10) -> None:
    for vermenigvuldiger in range(1, aantal+1):
        resultlaat = vermenigvuldiger * getal
        print(f'{vermenigvuldiger} x {getal} = {resultlaat}')

#print(vermenigvuldigingstafel(5, 10))
#Dit print de ingevulde tafel van het getal wat ingevoerd wordt