from test_lib import test, report
from math import floor, ceil, pow


def grootste(nr1: int, nr2: int) -> str:
    if nr1 == nr2:
        return f'Beide getallen zijn even groot (nr1: {nr1}, nr2: {nr2})'
    elif nr1 > nr2:
        return f'nr1 ({nr1}) is groter dan nr2 ({nr2})'
    else:
        return f'nr2 ({nr2}) is groter dan nr1 ({nr1})'


nr1 = 5
nr2 = 3
expect = f'nr1 ({nr1}) is groter dan nr2 ({nr2})'
name = f'test grootste: nr1={nr1} nr2={nr2}'
test(name, expect, grootste(nr1, nr2))

nr1 = 3
nr2 = 5
expect = f'nr2 ({nr2}) is groter dan nr1 ({nr1})'
name = f'test grootste: nr1={nr1} nr2={nr2}'
test(name, expect, grootste(nr1, nr2))
 
nr1 = 4
nr2 = 4
expect = f'Beide getallen zijn even groot (nr1: {nr1}, nr2: {nr2})'
name = f'test grootste: nr1={nr1} nr2={nr2}'
test(name, expect, grootste(nr1, nr2))
 
nr1 = 0
nr2 = 0
expect = f'Beide getallen zijn even groot (nr1: {nr1}, nr2: {nr2})'
name = f'test grootste: nr1={nr1} nr2={nr2}'
test(name, expect, grootste(nr1, nr2))
 
nr1 = -3
nr2 = -1
expect = f'nr2 ({nr2}) is groter dan nr1 ({nr1})'
name = f'test grootste: nr1={nr1} nr2={nr2}'
test(name, expect, grootste(nr1, nr2))
 
nr1 = 100
nr2 = 99
expect = f'nr1 ({nr1}) is groter dan nr2 ({nr2})'
name = f'test grootste: nr1={nr1} nr2={nr2}'
test(name, expect, grootste(nr1, nr2))
 
nr1 = -5
nr2 = -5
expect = f'Beide getallen zijn even groot (nr1: {nr1}, nr2: {nr2})'
name = f'test grootste: nr1={nr1} nr2={nr2}'
test(name, expect, grootste(nr1, nr2))
 
report()