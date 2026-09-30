import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from functions import getEarnings
from random import randint

character_test_1 = {
    'name': 'Bob',
    'ownsHorse': True,
    'adventuring': True,
    'cash': {'platinum': 0, 'gold': 1, 'silver': 7, 'copper': 5}
}

character_test_2 = {
    'name': 'Emma',
    'ownsHorse': True,
    'adventuring': True,
    'cash': {'platinum': 1, 'gold': 5, 'silver': 10, 'copper': 9}
}

friends = [
    {
        'name': 'Jorick',
        'shareWith': True,
        'adventuring': True,
        'cash': {'platinum': 0, 'gold': 9, 'silver': 9, 'copper': 43}
    },
    {
        'name': 'Grommel',
        'shareWith': True,
        'adventuring': True,
        'cash': {'platinum': 1, 'gold': 2, 'silver': 2, 'copper': 8}
    },
    {
        'name': 'Tristan',
        'shareWith': False,
        'adventuring': True,
        'cash': {'platinum': 0, 'gold': 2, 'silver': 17, 'copper': 11}
    },
    {
        'name': 'Massimo',
        'shareWith': True,
        'adventuring': True,
        'cash': {'platinum': 0, 'gold': 5, 'silver': 9, 'copper': 3}
    },
    {
        'name': 'Durbane',
        'shareWith': True,
        'adventuring': False,
        'cash': {'platinum': 1, 'gold': 5, 'silver': 12, 'copper': 11}
    },
    {
        'name': 'Otho',
        'shareWith': True,
        'adventuring': True,
        'cash': {'platinum': 0, 'gold': 1, 'silver': 2, 'copper': 7}
    }
]

investors = [
    {
        'name': 'Dwindel',
        'adventuring': True,
        'profitReturn': 9,
        'cash': {'platinum': 4, 'gold': 5, 'silver': 0, 'copper': 0}
    },
    {
        'name': 'Cipher',
        'adventuring': False,
        'profitReturn': 6,
        'cash': {'platinum': 2, 'gold': 20, 'silver': 0, 'copper': 0}
    },
    {
        'name': 'Maxxy',
        'adventuring': True,
        'profitReturn': 12,
        'cash': {'platinum': 8, 'gold': 50, 'silver': 100, 'copper': 0}
    }
]

expected = [{'name': 'Bob', 'start': 2.5, 'end': 56.67}]
result = getEarnings(100, character_test_1, friends, investors)
test('getEarnings - test 1',expected, result)

expected = [{'name': 'Emma', 'start': 32.18, 'end': 146.63}]
result = getEarnings(525.50, character_test_2, friends, investors)
test('getEarnings - test 2',expected, result)

expected = [{'name': 'Emma', 'start': 32.18, 'end': 1488.85}]
result = getEarnings(10000, character_test_2, friends, investors)
test('getEarnings - test 3',expected, result)

if __name__ == "__main__":
    report()