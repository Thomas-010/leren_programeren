def afronden_stuivers(bedrag: float) -> float:
    afronden_cent = 5
    return round(bedrag * 100 / afronden_cent) * afronden_cent / 100

print(afronden_stuivers(62.60))
print(afronden_stuivers(76.61))
print(afronden_stuivers(28.82))
print(afronden_stuivers(2.23))
print(afronden_stuivers(28.34))