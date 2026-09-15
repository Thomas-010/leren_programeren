# Controleert of een getal een priemgetal is.
def is_prime(number:int) -> bool:
    # Dit kijkt of het nummer kleiner is of gelijk is aan 1
    if number <= 1:
        return False
    
    # Dit kijkt of het nummer gelijk is aan 2
    if number == 2:
        return True
    
    # Dit kijkt of het nummer even is
    if number % 2 == 0:
        return False
    
    # Dit kijkt of het nummer deelbaar is door een oneven getal 
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    
    # Als geen van de voorwaarden klopt, dan is het een priemgetal
    return True

def get_first_primes(amount: int) -> list:
    priemgetal = []
    nummer = 2  # Start met het eerste priemgetal

    while len(priemgetal) < amount:
        if is_prime(nummer):
            priemgetal.append(nummer)
        nummer += 1

    return priemgetal

def get_primes_between(start: int, end: int) -> list:
    priemgetal = []

    for nummer in range(start, end + 1):
        if is_prime(nummer):
            priemgetal.append(nummer)

    return priemgetal

def get_primes_until(end: int) -> list:
    priemgetal = []

    for nummer in range(2, end + 1):
        if is_prime(nummer):
            priemgetal.append(nummer)

    return priemgetal