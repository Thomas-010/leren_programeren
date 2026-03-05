def vergelijk_getallen(nr1: int, nr2: int) -> str:
    if nr1 == nr2:
        return f'Beide getallen zijn even groot (nr1: {nr1}, nr2: {nr2})'
    elif nr1 > nr2:
        return f'nr1 ({nr1}) is groter dan nr2 ({nr2})'
    else:
        return f'nr2 ({nr2}) is groter dan nr1 ({nr1})'

print(vergelijk_getallen(5, 10))