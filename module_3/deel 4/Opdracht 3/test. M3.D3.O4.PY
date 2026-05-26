from test_lib import test, report

def controleer_gok(gok: int, geheim: int) -> bool:
    return gok == geheim

def geef_richtingshint(gok: int, geheim: int) -> str:
    if gok == geheim:
        return 'Geraden'
    elif gok < geheim:
        return 'Hoger'
    else:
        return 'Lager'

def geef_temperatuurhint(gok: int, geheim: int) -> str:
    verschil = abs(gok - geheim)
    if verschil < 20:
        return 'Je bent heel warm'
    if verschil < 50:
        return 'Je bent warm'
    else:
        return ''

def update_score(score: int, geraden: bool) -> int:
    if geraden:
        return score + 1
    return score

# Check gok
gok = 50
geheim = 50
expect_geraden = True
name = f'test controleer_gok: gok={gok} geheim={geheim}'
test(name, expect_geraden, controleer_gok(gok, geheim))

gok = 30
geheim = 50
expect_geraden = False
name = f'test controleer_gok: gok={gok} geheim={geheim}'
test(name, expect_geraden, controleer_gok(gok, geheim))

# Richtingsgint
gok = 30
geheim = 50
expect_hint = 'Hoger'
name = f'test richtingshint: gok={gok} geheim={geheim}'
test(name, expect_hint, geef_richtingshint(gok, geheim))

gok = 70
geheim = 50
expect_hint = 'Lager'
name = f'test richtingshint: gok={gok} geheim={geheim}'
test(name, expect_hint, geef_richtingshint(gok, geheim))

gok = 50
geheim = 50
expect_hint = 'Geraden'
name = f'test richtingshint: gok={gok} geheim={geheim}'
test(name, expect_hint, geef_richtingshint(gok, geheim))

# Temphint
gok = 35
geheim = 50
expect_temp = 'Je bent heel warm'
name = f'test temperatuurhint: gok={gok} geheim={geheim}'
test(name, expect_temp, geef_temperatuurhint(gok, geheim))

gok = 10
geheim = 50
expect_temp = 'Je bent warm'
name = f'test temperatuurhint: gok={gok} geheim={geheim}'
test(name, expect_temp, geef_temperatuurhint(gok, geheim))

gok = 500
geheim = 50
expect_temp = ''
name = f'test temperatuurhint: gok={gok} geheim={geheim}'
test(name, expect_temp, geef_temperatuurhint(gok, geheim))

# Score update
score = 0
geraden = True
expect_score = 1
name = f'test update_score: score={score} geraden={geraden}'
test(name, expect_score, update_score(score, geraden))

score = 3
geraden = False
expect_score = 3
name = f'test update_score: score={score} geraden={geraden}'
test(name, expect_score, update_score(score, geraden))

report()