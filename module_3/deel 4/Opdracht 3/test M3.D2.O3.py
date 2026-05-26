from test_lib import test, report
 
def afronden_stuivers(bedrag: float) -> float:
    afronden_cent = 5
    return round(bedrag * 100 / afronden_cent) * afronden_cent / 100


bedrag = 62.60
expected = 62.60
name = f'test afronden: bedrag={bedrag}'
test(name, expected, afronden_stuivers(bedrag))

bedrag = 76.61
expected = 76.60
name = f'test afronden: bedrag={bedrag}'
test(name, expected, afronden_stuivers(bedrag))

bedrag = 28.82
expected = 28.80
name = f'test afronden: bedrag={bedrag}'
test(name, expected, afronden_stuivers(bedrag))

bedrag = 2.23
expected = 2.25
name = f'test afronden: bedrag={bedrag}'
test(name, expected, afronden_stuivers(bedrag))

bedrag = 28.34
expected = 28.35
name = f'test afronden: bedrag={bedrag}'
test(name, expected, afronden_stuivers(bedrag))

bedrag = 2.24
expected = 2.25
name = f'test afronden: bedrag={bedrag}'
test(name, expected, afronden_stuivers(bedrag))

bedrag = 13.01
expected = 13.00
name = f'test afronden: bedrag={bedrag}'
test(name, expected, afronden_stuivers(bedrag))

bedrag = 0.00
expected = 0.00
name = f'test afronden: bedrag={bedrag}'
test(name, expected, afronden_stuivers(bedrag))

report()